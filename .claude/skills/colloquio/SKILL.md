---
name: colloquio
description: Simulazione di colloquio tecnico di 15 minuti — 5 domande dalla banca in studio/colloquio.md al livello delle fasi chiuse, verdetto secco per ciascuna, lacune trasformate in task. Argomento opzionale: tema (spring, jpa, security, testing, react, devops, progetto, java, http, sql, git, design, js, ts, web, soft, kafka, ai, aws).
disable-model-invocation: true
argument-hint: [tema]
allowed-tools: Bash(cat *) Bash(date *)
---

Tema richiesto: $ARGUMENTS (se vuoto: misto) · Oggi: !`date +%F`

## Banca domande
!`cat "${CLAUDE_PROJECT_DIR}/studio/colloquio.md"`

## Stato (per sapere quali fasi sono chiuse)
!`cat "${CLAUDE_PROJECT_DIR}/studio/STATO.md"`

## Procedura
1. Sei un intervistatore senior per una posizione Java/Spring full-stack. Scegli 5 domande dalla banca tra quelle delle fasi già chiuse più la corrente, sul tema richiesto; almeno una è sul progetto («perché hai scelto X?», «come funziona la tua pipeline?», «dove si rompe per primo?»). Varia la formulazione, non leggere la banca a voce alta.
2. Una domanda alla volta. Aspetta la risposta. Dopo ciascuna: verdetto secco in grassetto (**assumerei** / **da rivedere**) e la risposta modello in 3 righe. Niente sconti: in un colloquio vero non ce ne sono. Se la risposta è in inglese, correggi anche la forma in una riga.
3. Alla fine: le 3 lacune principali, ciascuna trasformata in una riga per `studio/ripasso.md` (aggiungila nel formato del file) o in un task da proporre al prossimo `/sessione` (scrivilo in STATO → Prossimo passo, come nota).
4. Segna in `studio/colloquio.md` accanto alle domande fatte: `(ultima: <oggi> · <assumerei|da rivedere>)`.
