---
name: bloccato
description: Lo studente è bloccato su un errore o un concetto. Hint progressivi — direzione, poi dettaglio, soluzione solo se la chiede esplicitamente. Argomento: messaggio d'errore o descrizione del blocco.
disable-model-invocation: true
argument-hint: [errore o descrizione]
allowed-tools: Bash(git status *) Bash(git diff *) Bash(git log *) Bash(git show *) Bash(cat *) Bash(date *)
---

Blocco descritto: $ARGUMENTS

## Procedura
1. Se manca, chiedi l'errore ESATTO (stack trace, log, output del comando) e guarda il diff recente (`git diff`). Leggi i file coinvolti. Non tirare a indovinare.
2. **Hint 1 — direzione**: dove guardare e quale concetto c'entra, in 3-5 righe; usa la mappa Java EE → Spring (`studio/fasi/F1.md`) se aiuta. Nessun codice. Poi fermati con: «Prova. Se non basta, rilancia `/bloccato`».
3. Se torna: **Hint 2 — dettaglio**: file e riga, cosa va cambiato a parole e perché. Al massimo un frammento di 1-3 righe se è pura sintassi. Poi fermati.
4. Solo se scrive «soluzione»: mostra il codice minimo che risolve, spiegato riga per riga, e registra in `studio/STATO.md` → Debito di apprendimento: `<data> — <tema> — soluzione mostrata da Claude, da rifare a mano al prossimo /ripasso`.
5. Se è sullo stesso blocco da più di 45 minuti (chiediglielo), salta direttamente all'Hint 2. Se è lo stesso errore per la terza volta: proponi di parcheggiare — scrivi il blocco in STATO → Blocchi aperti (cosa, perché, cosa serve) e chiudi la sessione con un task piccolo che si chiude in 20 minuti, per il morale.

Mai iniziare dal codice. Mai riscrivere il suo file. Se l'errore è di ambiente (versioni, Docker, rete, permessi), dillo subito: non è un suo errore di comprensione e non deve sentirlo come tale.
