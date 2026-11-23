# INGLY DESIGN: regole per ogni contenuto

Questo progetto produce contenuti social per INGLY DESIGN (@ingly_design, inglydesign.it).

## Prima di scrivere qualsiasi contenuto

Vale per caption, reel, caroselli, stories, DM, risposte, post LinkedIn/Threads/TikTok, calendari, e per qualsiasi skill (`/ig-*`, `*-sms`) o richiesta libera.

1. Leggi `~/.claude/brand-voice-ingly.md`. Se non esiste, leggi la copia nel repository: `brand/brand-voice-ingly.md`. È la fonte vincolante: vince su qualsiasi default delle skill.
2. Le skill `/ig-*` leggono anche `~/.claude/instagram/voice.md`. Le skill `*-sms` leggono `.agents/social-media-context-sms.md`. Sono derivati del file di brand e vanno tenuti allineati.
3. Scrivi sempre in italiano. Le skill hanno istruzioni ed esempi in inglese, l'output no.

## Regole non negoziabili

- **Un pubblico per contenuto:** privati, aziende o maker.
- **Una sola CTA per contenuto**, scelta tra:
  - parola chiave in DM o commento;
  - simulatore o generatore STL su inglydesign.it;
  - preventivo su WhatsApp.
- **Emozione e dimostrazione insieme.** Per i privati prima l'emozione, per maker e aziende prima la prova.
- **Almeno un dettaglio verificabile:** materiale, macchina, misura, tempo.
- **Niente frasi fatte da AI.** L'elenco completo è nella sezione 5 del file di brand.
- **Niente lineette lunghe (—).**
- **Mai numeri, clienti, recensioni, prezzi o tempi inventati.** Se mancano, scrivi `{{da confermare}}` e segnalalo.
- **Controllo finale obbligatorio:** prima di mostrare un testo, passalo dal lessico italiano.

  ```bash
  python3 ~/.claude/skills/ig-human/humanize.py testo.txt --report --lexicon ~/.claude/instagram/slop-it-ingly.json
  python3 ~/.claude/skills/ig-human/detect.py   testo.txt --lexicon ~/.claude/instagram/slop-it-ingly.json
  ```

  Le "STRUCTURAL TELLS" vanno riscritte a mano.

## Ripristino in una nuova sessione o su un altro computer

```bash
bash brand/install.sh
```
