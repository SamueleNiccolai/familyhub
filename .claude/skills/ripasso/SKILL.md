---
name: ripasso
description: Ripasso distanziato dalla banca domande in studio/ripasso.md — 2 domande in apertura di ogni /sessione, o un giro di 10 minuti quando lo studente lo chiede; una domanda alla volta, poi aggiorna date ed esiti.
allowed-tools: Bash(cat *) Bash(date *)
---

Oggi: !`date +%F`

## Banca domande
!`cat "${CLAUDE_PROJECT_DIR}/studio/ripasso.md"`

## Debito di apprendimento (da STATO)
!`cat "${CLAUDE_PROJECT_DIR}/studio/STATO.md"`

## Procedura
1. Scegli 3-5 domande (2 se il ripasso apre una `/sessione`) solo su argomenti già fatti — domande di fasi chiuse, o della fase corrente se la voce relativa è già spuntata nel file di fase: prima le `✗`, poi le mai fatte (`esito: —`), poi le più vecchie. Se in STATO c'è un item nel Debito di apprendimento, una delle domande è su quello: chiedigli di spiegarlo a parole o di rifarlo a mano.
2. Una domanda alla volta. Aspetta la risposta. Valuta in una riga (✓ giusto / ~ parziale / ✗ no) e correggi in massimo 2 righe. Niente lezioni: se una risposta è ✗, la lacuna diventa una nota per `/sessione`, non una spiegazione di 20 righe adesso.
3. Alla fine aggiorna in `studio/ripasso.md` le righe fatte (`ultima: <oggi> · esito: <✓/~/✗>`), e in `studio/STATO.md` → `Ultimo ripasso: sessione n° <N>` (N = sessione corrente). Se un item del debito è stato spiegato bene, rimuovilo dal debito.
4. Chiudi con: «Ripasso fatto. Torniamo al task» (o a `/sessione` se non è ancora partita).
