#!/usr/bin/env python3
"""Kit video INGLY: genera i cartelli 9:16 e monta il video finale.

  python3 render.py cartelli                       # crea i PNG in ../cartelli/
  python3 render.py video CLIP.mp4 instagram       # -> ../ingly_instagram.mp4
  python3 render.py video CLIP.mp4 tiktok --voce voce.m4a

Il clip viene portato a 1080x1920 (ritaglio centrale se è orizzontale) e
tagliato alla durata dello script. Con --voce l'audio originale viene
sostituito dalla voce registrata. Lo stesso file TikTok va bene per gli Shorts.
"""
import argparse, json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
CARDS = os.path.join(KIT, "cartelli")
W, H = 1080, 1920
SAFE_RIGHT = 230            # colonna destra coperta dai pulsanti
TEXT_Y = 330                # parte alta della zona sicura (230-1440)
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"


def load():
    with open(os.path.join(HERE, "cartelli.json"), encoding="utf-8") as f:
        return json.load(f)


def font(size):
    try:
        return ImageFont.truetype(FONT, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, f, maxw):
    """A capo automatico; "\n" nel testo forza un a capo."""
    lines = []
    for part in text.split("\n"):
        cur = ""
        for w in part.split():
            t = (cur + " " + w).strip()
            if draw.textlength(t, font=f) <= maxw or not cur:
                cur = t
            else:
                lines.append(cur); cur = w
        lines.append(cur)
    return lines


def card(text, path, size=78, y=TEXT_Y, fill=(0, 0, 0, 185), color="white"):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font(size)
    area_l, area_r = 60, W - SAFE_RIGHT
    lines = wrap(d, text, f, area_r - area_l - 80)
    lh = int(size * 1.18)
    boxw = max(d.textlength(l, font=f) for l in lines) + 80
    boxh = lh * len(lines) + 50
    cx = (area_l + area_r) / 2
    x0, y0 = cx - boxw / 2, y
    d.rounded_rectangle([x0, y0, x0 + boxw, y0 + boxh], radius=28, fill=fill)
    for i, l in enumerate(lines):
        tw = d.textlength(l, font=f)
        d.text((cx - tw / 2, y0 + 25 + i * lh), l, font=f, fill=color)
    img.save(path)


def make_cards():
    cfg = load()
    os.makedirs(CARDS, exist_ok=True)
    card(cfg["serie"], os.path.join(CARDS, "serie.png"), size=44, y=240,
         fill=(255, 255, 255, 230), color="black")
    out = []
    for canale in ("instagram", "tiktok"):
        for i, (a, b, t) in enumerate(cfg[canale]["cartelli"], 1):
            p = os.path.join(CARDS, f"{canale}_{i:02d}.png")
            card(t, p, y=TEXT_Y + 90)
            out.append(p)
    print(f"{len(out) + 1} cartelli in {CARDS}")


def make_video(clip, canale, voce=None, out=None):
    cfg = load()[canale]
    if not os.path.exists(os.path.join(CARDS, f"{canale}_01.png")):
        make_cards()
    out = out or os.path.join(KIT, f"ingly_{canale}.mp4")
    dur = cfg["durata"]
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", clip]
    if voce:
        cmd += ["-i", voce]
    first_card = 2 if voce else 1
    cmd += ["-i", os.path.join(CARDS, "serie.png")]
    for i in range(len(cfg["cartelli"])):
        cmd += ["-i", os.path.join(CARDS, f"{canale}_{i + 1:02d}.png")]
    fc = [f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps=30[v0]"]
    serie_idx = first_card
    fc.append(f"[v0][{serie_idx}:v]overlay=0:0:enable='between(t,0,2.9)'[v1]")
    last = "v1"
    for i, (a, b, _) in enumerate(cfg["cartelli"]):
        idx = serie_idx + 1 + i
        nxt = f"v{i + 2}"
        fc.append(f"[{last}][{idx}:v]overlay=0:0:enable='between(t,{a},{b})'[{nxt}]")
        last = nxt
    cmd += ["-filter_complex", ";".join(fc), "-map", f"[{last}]"]
    cmd += ["-map", "1:a?" if voce else "0:a?"]
    cmd += ["-t", str(dur), "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "csv=p=0", clip], capture_output=True, text=True)
    try:
        if float(probe.stdout.strip()) < dur:
            print(f"ATTENZIONE: il clip dura meno dello script ({dur}s): il video finirà prima.")
    except ValueError:
        pass
    subprocess.run(cmd, check=True)
    print("creato:", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("azione", choices=["cartelli", "video"])
    ap.add_argument("clip", nargs="?")
    ap.add_argument("canale", nargs="?", choices=["instagram", "tiktok"])
    ap.add_argument("--voce")
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.azione == "cartelli":
        make_cards()
    else:
        if not (a.clip and a.canale):
            sys.exit("uso: render.py video CLIP.mp4 instagram|tiktok [--voce file]")
        make_video(a.clip, a.canale, a.voce, a.out)
