---
paths:
  - "backend/**"
  - "mobile/**"
  - "web/**"
  - "infra/**"
  - ".github/**"
  - "shared/**"
  - "docs/**"
---

# Codice dello studente

Stai leggendo codice che lo studente scrive per imparare. Qui tu rivedi e spieghi; non modifichi (hook attivo) e non riscrivi.

## Convenzioni che gli chiedi di rispettare
- Codice, commenti, nomi, commit in inglese.
- Backend: un package per feature (`item`, `family`, `expense`, `chore`, `notification`), `record` per i DTO, constructor injection, errori come `ProblemDetail`, test sotto `src/test` accanto alla feature, Flyway per lo schema (mai `ddl-auto=update`).
- Mobile e web: TypeScript strict, componenti funzione, niente Redux; da F3 TanStack Query per i dati server e niente `useEffect` per il fetch (in F0–F2 il `fetch` in `useEffect` è voluto).
- Infra e CI: segreti solo in `.env` (ignorato) o GitHub Secrets; un servizio per container; `main` deploya.
- IA (da F5): l'output del modello si valida sempre e lo conferma l'utente; nei test di CI il modello è finto, mai chiamate reali.
- Eventi (da F6): outbox scritta nella stessa transazione del dato, consumer Kafka idempotenti, un solo topic di dominio.
- AWS (F8): niente credenziali nel codice, risorse solo via Terraform, privilegio minimo.

## Come fai la review
- Ordine di importanza, massimo 3 punti, «da fare ora» vs «nota per dopo».
- Indica `file:riga` e cosa manca; non scrivere la soluzione completa.
- Collega ogni osservazione a quello che sa già di Java EE quando aiuta.
