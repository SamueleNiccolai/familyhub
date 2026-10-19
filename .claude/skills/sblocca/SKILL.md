---
name: sblocca
description: Lo studente chiede esplicitamente che Claude scriva o modifichi codice del prodotto in questa sessione (boilerplate, setup, configurazione). Crea il flag che disattiva il blocco dell'hook e registra il debito di apprendimento. Argomento: motivo.
disable-model-invocation: true
argument-hint: [motivo]
allowed-tools: Bash(touch ${CLAUDE_PROJECT_DIR}/studio/.sblocca) Bash(date *)
---

Motivo: $ARGUMENTS

## Procedura
1. Se il motivo è vuoto, chiedilo: cosa devo scrivere e perché non lo scrive lui (tempo? setup noioso? troppo avanti per ora?). Se la risposta è «non so come si fa», proponi prima `/bloccato`: lo sblocco è per boilerplate e setup, non per il concetto che sta imparando. Se insiste, procedi: è una sua decisione.
2. Esegui esattamente: `touch ${CLAUDE_PROJECT_DIR}/studio/.sblocca` (il flag è ignorato da git, lo rimuove `/chiudi` e comunque scade dopo 6 ore).
3. Registra in `studio/STATO.md` → Debito di apprendimento: `<data> — <cosa scrivo> — scritto da Claude su richiesta; da leggere e spiegare a parole al prossimo /ripasso`.
4. Scrivi quello che ti ha chiesto, e solo quello, con commenti sulle scelte non ovvie. Prima di chiudere il task con `/fatto`, chiedigli di leggerlo e spiegartelo: se non ci riesce, è il task della prossima sessione.
