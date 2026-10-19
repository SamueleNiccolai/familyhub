---
name: chiudi
description: Chiude la sessione, anche a metà task — due righe nel diario, STATO aggiornato, promemoria commit, rimozione dello sblocco.
disable-model-invocation: true
allowed-tools: Bash(cat *) Bash(git status *) Bash(git diff *) Bash(git log *) Bash(date *) Bash(ls *) Bash(rm ${CLAUDE_PROJECT_DIR}/studio/.sblocca)
---

Oggi: !`date +%F`

## Stato
!`cat "${CLAUDE_PROJECT_DIR}/studio/STATO.md"`

## Modifiche non committate
!`git status --short`

## Procedura
1. Se esiste `studio/.sblocca` (controlla con `ls`), rimuovilo subito, prima di fare domande (il permesso di `allowed-tools` vale solo in questo turno): `rm ${CLAUDE_PROJECT_DIR}/studio/.sblocca`.
2. Chiedi (o proponi tu, se ha fretta): cosa hai fatto oggi? quante ore? cosa fai la prossima volta? Il «prossima volta» deve essere una frase eseguibile in 10 minuti al rientro (es. «riaprire `ItemControllerTest` e far passare il test del 400»), perché il costo di rientro è il motivo n.1 per cui si smette.
3. Scrivi in `studio/DIARIO.md`: `## <oggi> · s<N> · <ore>h`, poi `fatto:` e `prossima volta:`. Anche se oggi è andata male: «fatto: niente, bloccato su X» è un'informazione. Se `/fatto` ha già scritto la voce di oggi, aggiornala invece di crearne un'altra.
4. Aggiorna `studio/STATO.md`: task aperto (resta aperto se non chiuso, con il punto esatto raggiunto), prossimo passo, ore cumulate, data.
5. Se ci sono modifiche non committate, proponi il messaggio di commit (inglese, Conventional Commits) e ricordagli di committare: il commit lo fa lui. Se è su un branch da PR, ricorda anche il push.
6. Saluta in una riga. Nessuna lezione in chiusura.
