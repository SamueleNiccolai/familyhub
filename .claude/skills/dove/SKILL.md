---
name: dove
description: Mostra dove sono nel percorso (fase, blocco, task aperto, prossimo passo, ritardo sul calendario). Da usare rientrando dopo giorni di pausa o quando lo studente chiede "a che punto siamo".
allowed-tools: Bash(cat *) Bash(tail *) Bash(date *)
---

Oggi: !`date +%F`

## Stato
!`cat "${CLAUDE_PROJECT_DIR}/studio/STATO.md"`

## Ultime voci del diario
!`tail -n 15 "${CLAUDE_PROJECT_DIR}/studio/DIARIO.md"`

## Cosa fare
Rispondi in 6-8 righe, in italiano, senza preamboli:
- fase e blocco correnti;
- task aperto (se c'è) e prossimo passo concreto, copiati da STATO;
- giorni passati dall'ultima sessione (dalla data in STATO o dall'ultima voce del diario);
- se la data di oggi supera la fine prevista della fase (calendario di STATO) di oltre metà della sua durata, dillo e proponi `/ricalibra`; se la supera di meno, segnala solo il ritardo;
- chiudi con «`/sessione [ore]` quando vuoi».

Non fare altro: niente lezioni, niente task nuovi.
