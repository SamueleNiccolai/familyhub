---
name: sessione
description: Avvia la sessione di studio di oggi — legge lo stato, propone UN task dimensionato per le ore disponibili con criterio di fatto verificabile, aggiorna STATO. Argomento opzionale: ore disponibili (default 3).
disable-model-invocation: true
argument-hint: [ore]
allowed-tools: Bash(cat *) Bash(tail *) Bash(date *)
---

Ore disponibili oggi: $ARGUMENTS (se vuoto: 3). Oggi: !`date +%F`

## Stato
!`cat "${CLAUDE_PROJECT_DIR}/studio/STATO.md"`

## Ultime voci del diario
!`tail -n 10 "${CLAUDE_PROJECT_DIR}/studio/DIARIO.md"`

## Banca ripasso
!`cat "${CLAUDE_PROJECT_DIR}/studio/ripasso.md"`

## Procedura
1. Apri il file della fase corrente (`studio/fasi/F<n>.md`), individua il blocco corrente e il primo item non spuntato. Se in STATO c'è un task aperto, si riparte da quello, dal punto esatto in cui era rimasto.
2. Apri con 2 domande di ripasso dalla banca qui sopra, solo su argomenti già fatti: fasi chiuse, o voci già spuntate nel file della fase corrente (procedura di `/ripasso`, 3 minuti: una alla volta, esito annotato). Se non ce ne sono, salta.
3. Se le ore sulla fase superano 1,5× la stima del file di fase, o la data supera la fine fase del calendario di oltre metà della sua durata: dillo in una riga e proponi `/ricalibra` prima di partire. Se accetta, fermati lì. Un ritardo minore si segnala e basta.
4. Proponi UN task che stia nelle ore disponibili, in questo formato e niente altro:
   - **Task** — una frase.
   - **Perché adesso** — una riga che lo lega al blocco e al prodotto.
   - **Passi** — massimo 5, concreti, in ordine; il primo deve essere eseguibile in 5 minuti.
   - **Teoria JIT** — al massimo UNA risorsa, max 20 minuti, con cosa cercarci; oppure «nessuna, oggi solo pratica».
   - **Criterio di fatto** — un comando o un'osservazione verificabile (es. `./mvnw verify` verde con il nuovo test; la lista appare sul telefono; `curl ...` risponde 400 ProblemDetail).
   - **Rischio tipico** — dove si perde tempo e cosa fare quando succede.
   - **Stima** — ore.
5. Aggiorna `studio/STATO.md`: `Task aperto: <Task> — criterio di fatto: <criterio> — stima <h> h (dal <data>)`, sessione n° (+1, solo se l'ultima sessione registrata non è di oggi), data di oggi. Il prossimo passo resta invariato finché il task non è chiuso con `/fatto`.
6. Poi fermati e aspetta. Durante il lavoro rispondi con hint progressivi (CLAUDE.md, regola n.1). Non scrivere il codice del task.

Se il task non sta nelle ore: dividilo e proponi solo la prima metà. Se lo studente propone un task diverso, va bene purché sia nel blocco corrente; altrimenti spiega perché l'ordine conta e lascia decidere a lui.
