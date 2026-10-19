---
name: fatto
description: Lo studente dichiara concluso il task aperto. Verifica con i comandi, code review indipendente con l'agente revisore, spunta l'item, aggiorna STATO e DIARIO, aggiunge domande di ripasso; a fine fase avvia la chiusura. Argomento opzionale: note o percorso delle evidenze.
disable-model-invocation: true
argument-hint: [note]
allowed-tools: Bash(cat *) Bash(git status *) Bash(git diff *) Bash(git log *) Bash(git ls-files *) Bash(git show *) Bash(date *)
---

Note dello studente: $ARGUMENTS · Oggi: !`date +%F`

## Stato
!`cat "${CLAUDE_PROJECT_DIR}/studio/STATO.md"`

## Modifiche nel working tree
!`git status --short`

## Procedura
1. Ricava dal task aperto in STATO il criterio di fatto. Se non è verificabile con un comando o un'osservazione, chiedi l'evidenza (screenshot in `studio/evidenze/`, log, URL) prima di continuare.
2. **Verifica tu**: esegui i comandi del criterio (test, build, `curl`, `git diff`, `git log`). Niente fiducia sulla parola. Se qualcosa non gira, fermati qui: il task resta aperto; di' cosa manca in modo concreto (comando, output atteso vs ottenuto).
3. **Review indipendente**: lancia l'agente `revisore` passandogli SOLO (a) il criterio di fatto copiato da STATO, (b) come ottenere il diff completo: `git status --short`; poi `git diff main...HEAD` se su branch, altrimenti `git diff HEAD`; più i file nuovi elencati da `git ls-files --others --exclude-standard`, da leggere per intero, (c) l'eventuale URL o evidenza. Non passargli la conversazione né il tuo giudizio. Riporta allo studente BLOCCANTI / DUBBI / OK / LEZIONE così come arrivano, più al massimo 2 osservazioni tue se aggiungono qualcosa.
4. Se ci sono BLOCCANTI: il task resta aperto. Indica cosa correggere (`file:riga`, cosa manca), non la soluzione. Torna al punto 2 quando rilancia `/fatto`.
5. Se è tutto verde:
   - spunta l'item nel file di fase (`- [x] ... (YYYY-MM-DD)`);
   - aggiorna `studio/STATO.md`: task aperto → nessuno; prossimo passo → prossimo item non spuntato; ore cumulate (chiedi quante ore ha fatto, o stima dal task); scostamento rispetto al calendario;
   - scrivi in `studio/DIARIO.md` la voce della sessione nel formato del file (`## <oggi> · s<N> · <ore>h`, poi `fatto:` e `prossima volta:`): proponila tu, lui conferma o corregge; se poi lancia `/chiudi`, si aggiorna questa voce, non se ne crea un'altra;
   - aggiungi 1-2 domande sul concetto del task a `studio/ripasso.md`, nel formato del file;
   - proponi il messaggio di commit (inglese, Conventional Commits). Il commit lo fa lui.
6. Se era l'ultimo item della fase: avvia la **chiusura fase** descritta in fondo al file della fase — test di Feynman (una domanda alla volta, aspetta la risposta, valuta), review d'insieme con il `revisore` sul diff di tutta la fase con il DoD come criterio, tag (lo crea lo studente: `git tag -a v0.<n>-F<n> -m "…"` e `git push --tags`), revisione delle domande della fase in `studio/colloquio.md` (1-2 nuove nate dalla fase), STATO → fase successiva, blocco B1. La spiegazione Feynman ha al massimo 2 tentativi: se al secondo non regge, si passa comunque, con la lacuna in STATO → Debito di apprendimento e una domanda in `studio/ripasso.md`.

Tono: senior ma dalla sua parte. Prima cosa funziona, poi cosa migliorare: massimo 3 punti, «da fare ora» vs «nota per dopo».
