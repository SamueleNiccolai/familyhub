# STATO — una pagina, sempre aggiornata

Aggiornato: 2026-10-19 (sessione 0 — creazione del repo, validazione e ricalibrazione)

## Dove sono
- Fase: **F0 — Avvio** (sett. 1-2 · 19 ott – 1 nov 2026 · stima 16 h · capacità 24 h)
- Blocco: **B1 — Ambiente**
- Sessione n°: 0 · Ore cumulate: 0 · Ore sulla fase: 0
- Ultimo ripasso: — (2 domande in apertura di ogni sessione, solo su argomenti già fatti)
- Task aperto: nessuno → al prossimo `/sessione` parte F0/B1

## Prossimo passo
JDK 21 (SDKMAN, oppure il JDK 25 già installato compilando per 21: decidere), IntelliJ IDEA Ultimate già installato (ESLint e Prettier attivi, completamento IA multi-riga spento), Node LTS (nvm), Docker già ok; Expo Go su iPhone e Android con account Expo.

## Calendario (12 h/settimana in 3 sessioni; settimane leggere da 4 h: 21/12, 28/12, 29/3, 9/8, 16/8)
- F0 Avvio · 19 ott – 1 nov 2026
- F1 Spring Boot core · 2 nov – 6 dic 2026
- F2 Produzione · 7 dic 2026 – 10 gen 2027 (Natale leggero)
- F3 React + Expo · 11 gen – 21 feb 2027
- F4 Sicurezza e famiglie · 22 feb – 4 apr 2027 → **checkpoint CV e portfolio**
- F5 Dominio da colloquio e IA · 5 apr – 16 mag 2027
- F6 Rilascio mobile ed eventi (Kafka) · 17 mag – 27 giu 2027
- F7 Web + infra · 28 giu – 8 ago 2027 → `v1.0`
- F8 AWS + certificazione e consolidamento · 9 ago – 17 ott 2027 (Ferragosto leggero)

## Scostamento
In linea. (Regola: se le ore sulla fase superano 1,5× la stima, o la data supera la fine fase di oltre metà della sua durata → `/ricalibra`.)

## Debito di apprendimento
(codice scritto o mostrato da Claude, da ripassare — vuoto)

## Decisioni
- 2026-10-19 — Monorepo: `backend/ mobile/ web/ infra/` + `studio/`. Codice e commit in inglese, studio in italiano.
- 2026-10-19 — Il codice del prodotto lo scrive lo studente; Claude fa da mentore (hook attivo, `/sblocca` per le eccezioni, debito tracciato qui).
- 2026-10-19 — iOS resta in Expo Go finché non si decide l'Apple Developer (99 $/anno, necessario anche per una dev build), decisione rimandata a F6.
- 2026-10-19 — Validazione indipendente: applicati i 10 BLOCCANTI di `studio/VALIDAZIONE-2026-10-19.privato.md` (non committato; branch `validazione`); i DA MIGLIORARE sono da decidere.
- 2026-10-19 — IA: scansione di scontrini e bollette in F5 con Spring AI e un modello multimodale via API (bozza da confermare, immagini non conservate); in F8 passa ad Amazon Bedrock.
- 2026-10-19 — Kafka: un solo flusso in F6 (outbox → topic → consumer idempotente → push), dentro il monolite; ripiego se F6 sfora: eventi Spring interni.
- 2026-10-19 — AWS in F8 (account aperto solo allora: il free plan dura 6 mesi): S3, IAM, Bedrock, Budgets con Terraform; certificazione Developer – Associate DVA-C03 (150 $); SAA-C03 opzionale dopo ottobre 2027, non insieme. Terraform passa da F7 (hcloud) a F8 (AWS).
- 2026-10-19 — Percorso completo: 12 h/settimana in 3 sessioni con 5 settimane leggere; stime realistiche per blocco e margine in ogni fase; 1 h/settimana per CV e portfolio dal checkpoint. Applicati anche i DA MIGLIORARE della validazione (Java/SQL/HTTP, JS/TS, storie da colloquio, ripasso a ogni sessione, sicurezza F2–F7, DoD verificabili).
- 2026-10-19 — IDE: IntelliJ IDEA Ultimate (All Products Pack). Gli strumenti MCP di IntelliJ che scrivono file o eseguono comandi sono vietati in `.claude/settings.json`; l'SQL dall'IDE chiede conferma.
- 2026-10-19 — Repo pubblico su GitHub: https://github.com/SamueleNiccolai/familyhub (branch principale `main`; secret scanning e push protection attivi).
- 2026-10-19 — Repo pubblico: obiettivo personale e registri stanno in `CLAUDE.local.md` e `studio/*.privato.md`, non committati.
- (da prendere in F2) Hosting: VPS (tetto 10 €/mese) vs gratis (Render + DB esterno / Oracle).

## Blocchi aperti
nessuno
