---
documento: Funnel e automazioni commento -> DM
last_updated: 2026-11-23
---

# Funnel e automazioni

## 1. Parole chiave standard

Le parole chiave valgono solo su Instagram. Su Facebook vale "WhatsApp, sito o Demo Room"; su TikTok e YouTube vale una domanda nei commenti o il link.

Le parole chiave valgono sia nei commenti sia nei DM e non distinguono maiuscole e minuscole ("foto", "Foto", "FOTO").

| Parola | Quando la usi | Cosa riceve chi la scrive | Destinazione | Pubblico |
|---|---|---|---|---|
| **FOTO** | Serie A, regali, simulatore, post fissato 3 | Link al simulatore "Prova la tua foto incisa" + link al generatore STL di litofanie | `{{url simulatore}}?utm_source=instagram&utm_medium=dm&utm_campaign=foto` | Privati |
| **XTOOL** | Serie C, Serie B quando la macchina è protagonista, Demo Room | Info su Demo Room (Palermo, Sud Italia), modelli disponibili, consulenza, assistenza, link per prenotare | `{{link prenotazione demo}}` oppure WhatsApp 329 690 4627 | Maker, aziende |
| **PREVENTIVO** | Serie D, lavori B2B, gadget, targhe, piccoli lotti | Contatto diretto WhatsApp con messaggio precompilato | `https://wa.me/393296904627?text=Ciao%20INGLY%2C%20vorrei%20un%20preventivo` | Aziende, privati |

**Parole già usate in precedenza** (le reindirizzo per non perdere nessuno):
- **LASER** → stesso messaggio di FOTO;
- **C1** e **M2** → stesso flusso di XTOOL, con la scheda del modello in testa.

## 2. Messaggi automatici

I messaggi sono scritti con le regole del brand e verificati con il lessico anti-AI. `{{...}}` = da completare prima di attivare.

**FOTO**

```
Ciao! Ecco il simulatore per vedere la tua foto incisa prima di ordinarla: {{url simulatore}}

Se vuoi una litofania, qui c'è il generatore gratuito di file STL: {{url generatore STL}}

Hai un dubbio su una foto? Mandacela qui: ti diciamo come verrà.
```

**XTOOL**

```
Ciao! Siamo host ufficiali xTool Squad con Demo Room in Sicilia: puoi vedere le macchine lavorare dal vivo, anche con il tuo materiale.

Prenota la demo qui: {{link prenotazione demo}}
Oppure scrivici su WhatsApp: 329 690 4627

Dimmi solo che macchina ti interessa e per cosa vorresti usarla.
```

**PREVENTIVO**

```
Ciao! Per il preventivo ci serve sapere: cosa vuoi personalizzare, quanti pezzi, materiale e misura (anche indicativi).

Scrivici direttamente su WhatsApp, il messaggio è già pronto: https://wa.me/393296904627?text=Ciao%20INGLY%2C%20vorrei%20un%20preventivo
```

**Risposta pubblica al commento** (a rotazione, per non sembrare un bot):
- "Ti ho scritto in DM 📩"
- "Fatto, controlla i messaggi!"
- "Mandato, guarda in DM"

## 3. Strumenti per piattaforma

| Piattaforma | Automazione commento → DM | Come |
|---|---|---|
| **Instagram** | Sì | Meta Business Suite (Posta in arrivo, Automazioni), se il vostro account ha le risposte automatiche ai commenti; altrimenti uno strumento partner Meta che usa le API ufficiali (es. ManyChat). Mai app non ufficiali: rischio blocco account. |
| **Facebook** | Sì, verso Messenger | Stesso strumento di Instagram. Su Facebook la risposta porta a WhatsApp, al preventivo sul sito o alla Demo Room, non a parole chiave. |
| **TikTok** | Limitata | Nel DM si possono impostare messaggio di benvenuto e risposte a parole chiave, se l'account Business le ha; i commenti non mandano DM automatici. CTA: domanda nei commenti, link in bio. |
| **YouTube** | No | Commento fissato con il link e link nella descrizione. Negli Shorts, collegamento al video lungo correlato. |

**Regole Meta da rispettare:**
- un solo messaggio automatico per commento;
- niente follow-up automatici dopo 24 ore dall'ultima interazione dell'utente;
- i follow-up li fa una persona, a mano.

## 4. Il funnel completo

```
SCOPERTA        TikTok, YouTube Shorts, Reel (Serie B e A)
    ↓
FOLLOW          episodio numerato + "nel prossimo..." + profilo ottimizzato (bio, 3 fissati)
    ↓
CONVERSAZIONE   parola chiave (FOTO / XTOOL / PREVENTIVO), domanda nei commenti
    ↓
PROVA           simulatore, generatore STL, Demo Room
    ↓
CONTATTO        WhatsApp 329 690 4627
    ↓
ORDINE          preventivo, produzione, spedizione
    ↓
CONTENUTO       con il consenso del cliente, l'ordine diventa un episodio di Serie A o D
```

## 5. Misurazione

- **UTM su ogni link**
  - `utm_source`: instagram, facebook, tiktok, youtube;
  - `utm_medium`: bio, dm, descrizione, commento;
  - `utm_campaign`: foto, xtool, preventivo, nome della serie.
- **Ogni lunedì**, nella tabella sotto, metti in fila:
  1. parole chiave ricevute;
  2. click;
  3. conversazioni WhatsApp;
  4. preventivi;
  5. ordini.
- **Dove guardare:** se tante parole chiave non diventano click, va migliorato il messaggio. Se tanti click non diventano WhatsApp, va migliorato il sito o il simulatore.

| Settimana | FOTO | XTOOL | PREVENTIVO | Click sito | WhatsApp aperti | Demo prenotate | Ordini |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 6. Da completare prima di attivare

- [ ] `{{url simulatore}}`, `{{url generatore STL}}`
- [ ] `329 690 4627` e link wa.me
- [ ] `{{link prenotazione demo}}` (anche solo WhatsApp, se non avete un calendario online)
- [ ] Scelta strumento di automazione e test con un account secondario prima di pubblicare
