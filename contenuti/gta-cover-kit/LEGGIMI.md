# Kit pubblicazione: "La tua foto in copertina stile GTA VI" (Serie A, Ep. 01)

Tutto quello che serve per pubblicare su Instagram, Facebook, TikTok e YouTube.
Script, scelte e motivazioni sono in `../2026-11-23_cover-stile-gta.md`.

## Cosa c'è nel kit

| Cartella / file | Cosa contiene |
|---|---|
| `testi/` | Un file per canale, pronto da copiare e incollare |
| `cartelli/` | Testo a schermo in PNG trasparenti 1080x1920, già nella zona sicura: `instagram_01-09`, `tiktok_01-07`, `serie` |
| `tools/render.py` | Monta il video finale: cartelli agli orari giusti, formato 9:16, durata esatta |
| `tools/cartelli.json` | Testi e orari dei cartelli (modificabili) |

## Passo 1: girare (10 minuti)

Usate una cover nuova con **grafica originale**: niente logo e scritta "Grand Theft Auto", niente personaggi del gioco. Usate la foto di chi vi ha dato il consenso.

- **Formato:** telefono in **verticale**, 4K o 1080p, 30 fps.
- **Durata:** almeno 30 secondi di girato, una ripresa continua oppure clip già montate in ordine.
- **Ordine delle riprese**, che segue i cartelli:
  1. **Cover girata lentamente nella luce radente.** Si vede il rilievo, è l'hook.
  2. **Foto originale** sullo schermo del telefono.
  3. **Illustrazione** sullo schermo del PC.
  4. **Zoom** sui riquadri.
  5. **Stampante UV** al lavoro.
  6. **Macro raso superficie** con il dito che passa sul rilievo.
  7. **Cover nel pacco.**
  8. **Cover in mano**, inquadratura finale.
- **Voce:** registratela a parte leggendo lo script (Instagram 24,7 s, TikTok 14,2 s), oppure usate solo musica e cartelli.

## Passo 2: montare il video

**Opzione A: me lo mandi e lo monto io.** Carica qui il girato (ed eventualmente la voce). Ti restituisco:

- `ingly_instagram.mp4`: 24,7 s, per Reel Instagram e Facebook;
- `ingly_tiktok.mp4`: 14,2 s, per TikTok e YouTube Shorts.

**Opzione B: lo monti tu (CapCut o simili).** Importa i PNG di `cartelli/` come sovrapposizioni a tutto schermo, con questi orari:

| Instagram/FB | | TikTok/Shorts | |
|---|---|---|---|
| 0:00-2:9 | `serie` + `instagram_01` TU, IN COPERTINA | 0:00-2:9 | `serie` + `tiktok_01` STILE GTA VI, FACCIA TUA |
| 2:9-4:4 | `instagram_02` 1 FOTO | 2:9-4:4 | `tiktok_02` 1 FOTO |
| 4:4-6:5 | `instagram_03` → COPERTINA DA VIDEOGIOCO | 4:4-6:2 | `tiktok_03` → COPERTINA |
| 6:5-9:1 | `instagram_04` I TUOI AMICI NEI RIQUADRI | 6:2-7:6 | `tiktok_04` STAMPA UV |
| 9:1-12:7 | `instagram_05` STAMPA UV | 7:6-9:4 | `tiktok_05` GUARDA LA LUCE |
| 12:7-13:8 | `instagram_06` GUARDA LA LUCE | 9:4-11:3 | `tiktok_06` RILIEVO VERO |
| 13:8-17:4 | `instagram_07` RILIEVO VERO | 11:3-14:2 | `tiktok_07` DI CHI È LA PROSSIMA? |
| 17:4-19:9 | `instagram_08` SPEDIAMO IN TUTTA ITALIA | | |
| 19:9-24:7 | `instagram_09` SCRIVI "PREVENTIVO" | | |

(Orari in secondi e decimi: 2:9 = 2,9 s.)

**Opzione C: da computer con Python e ffmpeg.**

```bash
python3 tools/render.py video girato.mp4 instagram --voce voce_ig.m4a
python3 tools/render.py video girato.mp4 tiktok    --voce voce_tt.m4a
```

## Passo 3: prima di pubblicare (checklist)

- [ ] Nel video **non** ci sono logo, scritte o personaggi ufficiali del gioco.
- [ ] Consenso scritto della persona ritratta sulla cover.
- [x] Numero WhatsApp (329 690 4627), firma "Ingly Design" e nessuna scadenza d'ordine: già inseriti nei testi.
- [ ] Automazione **PREVENTIVO** attiva su Instagram, con il messaggio in `~/.claude/ingly-growth/funnel-automation.md` e il numero WhatsApp.
- [ ] Il testo per i gruppi maker descrive bene la vostra tecnica di rilievo (altrimenti correggetelo).
- [ ] Il numero di episodio è giusto (il kit usa "EP. 01").

## Passo 4: pubblicare in quest'ordine

| Quando | Canale | File video | Testo | Dove |
|---|---|---|---|---|
| Sera X, ore `{{ora}}` | Instagram Reel + Facebook Reel | `ingly_instagram.mp4` | `1_instagram_caption.txt` (IG) e `3_facebook_pagina.txt` (FB) | Meta Business Suite, un solo post con testo personalizzato per piattaforma |
| Sera X, +1 ora | TikTok | `ingly_tiktok.mp4` | `2_tiktok_caption.txt` | App TikTok: aggiungi un suono di tendenza dalla libreria commerciale |
| Sera X, +1 ora | YouTube Short | `ingly_tiktok.mp4` | `6_youtube_short.txt` | YouTube Studio |
| Giorno dopo | Gruppi Facebook locali e gamer | `ingly_instagram.mp4` (caricato, non condiviso) | `4_facebook_gruppi_locali.txt` | A mano, rispettando il regolamento del gruppo |
| 2 giorni dopo | Gruppi maker e stampa UV | foto macro del rilievo | `5_facebook_gruppi_maker.txt` | A mano |

**Prime 48 ore:**
- rispondere a tutti i commenti;
- mandare il DM a chi scrive PREVENTIVO, se l'automazione non è attiva;
- su TikTok, rispondere con un video ai commenti con un nome: diventano gli episodi successivi.
