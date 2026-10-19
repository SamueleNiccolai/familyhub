# PIANO — da Java EE a un prodotto Spring + React Native in produzione

Obiettivo: entro ottobre 2027, un profilo da senior su stack moderno, dimostrato da un prodotto completo costruito da me: backend Spring Boot, app iOS/Android con Expo, dashboard web React, test a tre livelli, Docker, CI/CD, una feature IA (Spring AI), un flusso event-driven (Kafka) e una parte AWS con certificazione.
Ritmo: 12 ore a settimana in 3 sessioni fisse (es. 3 + 4 + 5 h), con 5 settimane leggere da una sola sessione di 4 h (Natale ×2, Pasquetta, Ferragosto ×2). Inizio: 19 ottobre 2026.
Questo file è il riferimento; la memoria viva è `STATO.md`. Ogni fase ha il suo file in `fasi/`.

## Mappa in 10 righe
1. Progetto filo rosso: **FamilyHub**, gestionale per famiglie. Lista spesa condivisa → spese e budget mensile, con scansione IA di scontrini e bollette → famiglie con inviti → turni, scadenze e promemoria push via Kafka → dashboard web → AWS. Lo usa davvero la mia famiglia: utenti reali sono l'antidoto al «non avevo un vero obiettivo» con cui ho mollato Go e Flutter.
2. Ordine: prima Spring Boot (è il requisito dei colloqui, e Java EE lo rende una discesa: JPA uguale, CDI → DI, JAX-RS → Spring MVC), poi React/Expo. Ma in settimana 1 vedo già la lista sul telefono.
3. Deploy e pipeline alla fase 2 (inizio gennaio 2027): da lì in poi tutto si costruisce su un sistema in produzione.
4. React lo imparo una volta (react.dev) e lo spendo due volte: app mobile con Expo e, in F7, dashboard web con Vite — quella che i colloqui chiedono. Niente Expo-web come scorciatoia: ai colloqui chiedono DOM, CSS, routing web.
5. Checkpoint CV e portfolio a fine F4 (inizio aprile 2027): CV aggiornato, storie tecniche pronte, README da recruiter. Da lì 1 h a settimana va a questo fronte (dettagli nei file privati). Non si aspetta il mese 12.
6. Ore: ~390 h stimate da F0 a F7, con margine in ogni fase (capacità 462 h); in totale 584 h disponibili. Il core finisce l'8 agosto 2027; da lì AWS con certificazione (≈65 h) e buffer di consolidamento.
7. Se una fase sfora 1,5×, si taglia in quest'ordine: Terraform → Prometheus/Grafana → build iOS → Kafka (→ eventi Spring) → push → certificazione AWS (a dopo ottobre 2027). Mai la dashboard web, mai i test.
8. Non ora: Kubernetes, microservizi, Spring Cloud, Kafka Streams, WebFlux, GraphQL, Kotlin, Next.js, Redux, codice nativo, chatbot e RAG. Kafka entra in F6 per un solo flusso. Go e Flutter: archiviati senza rimpianti.
9. Costi: VPS (i prezzi Hetzner sono saliti nel 2026: verificare in F2, tetto 10 €/mese), API del modello IA (centesimi a scontrino, tetto mensile sul provider), esame AWS 150 $ (F8; l'uso di AWS sta nei crediti del free plan) e, solo se vorrò TestFlight/App Store, 99 $/anno Apple. Gli IDE sono già coperti dal mio All Products Pack. Opzioni gratuite indicate dove esistono.
10. Ritmo: 3 sessioni fisse; ogni sessione si apre con 2 domande di ripasso (3 minuti). Fine fase = spiego il concetto chiave a voce (Feynman) + code review d'insieme, poi si passa oltre.

## Come si lavora in questo repo (il metodo)
1. `claude` nella cartella del repo. Ogni sessione: `/sessione [ore]` → lavoro → `/fatto` oppure `/chiudi`. Rientrando dopo giorni: `/dove`.
2. Il codice lo scrivo io. Claude spiega, indica, verifica, rivede. Un hook gli impedisce di scrivere fuori da `studio/` e `.claude/` (gli strumenti MCP dell'IDE che scrivono sono vietati in `settings.json`); `/sblocca` lo disattiva per una sessione (al massimo 6 ore) e registra il debito in STATO.
3. «Fatto» = comando che gira + test verdi + diff rivisto dall'agente `revisore`, che vede solo il criterio e il diff (file nuovi compresi).
4. Bloccato: `/bloccato` con l'errore esatto → direzione → dettaglio → soluzione solo se la chiedo. Sopra i 45 minuti sullo stesso errore si passa al dettaglio; alla terza volta si parcheggia.
5. Ogni sessione parte con 2 domande di ripasso (3 min); `/ripasso` (10 min) quando serve un giro più lungo. Fine fase: Feynman (al massimo 2 tentativi) + review d'insieme + tag + domande in `colloquio.md`.
6. Se una fase sfora 1,5× → `/ricalibra`: si taglia scope nell'ordine indicato, non si spinge.

## Fasi (settimane · date · deliverable · verifica)
- **F0 Avvio** · 1-2 · 19 ott – 1 nov 2026 · lista hardcoded da Spring Boot visibile su iPhone e Android · screenshot + repo
- **F1 Spring Boot core** · 3-7 · 2 nov – 6 dic · CRUD lista spesa su Postgres, testato, + allenamento Java/SQL/HTTP · `./mvnw verify` verde con Testcontainers
- **F2 Produzione** · 8-12 · 7 dic – 10 gen 2027 (Natale leggero) · API live in HTTPS, pipeline GitHub Actions · push su main → deploy automatico
- **F3 React + Expo** · 13-18 · 11 gen – 21 feb · app a 2 schermate, API tipizzata · test componenti in CI, flow Maestro
- **F4 Sicurezza e famiglie** · 19-24 · 22 feb – 4 apr · login, famiglie, inviti, JWT · 2 account stessa lista, un terzo no · **checkpoint CV e portfolio**
- **F5 Dominio da colloquio e IA** · 25-30 · 5 apr – 16 mag · spese + report mensile, scansione IA di scontrini e bollette, OpenAPI, Actuator · 20 domande Spring risposte a voce, ≥8/10 scontrini letti giusti
- **F6 Rilascio mobile ed eventi** · 31-36 · 17 mag – 27 giu · push via Kafka (outbox → consumer idempotente), build EAS, update OTA · la famiglia installa la build e riceve una push, senza doppioni
- **F7 Web + infra** · 37-42 · 28 giu – 8 ago · dashboard React, Grafana, backup · dashboard live in HTTPS + restore provato · `v1.0`
- **F8 AWS e consolidamento** · 43-52 · 9 ago – 17 ott 2027 (Ferragosto leggero) · AWS nel progetto (S3, IAM, Bedrock, Terraform) + certificazione DVA-C03, portfolio · certificazione superata, portfolio pronto

Il dettaglio di ogni fase (blocchi, DoD, teoria JIT, risorse, trappole, chiusura) è in `fasi/F<n>.md`.

## Stack e versioni
Le versioni qui sotto sono quelle che assumo a ottobre 2026: **verificarle sui siti ufficiali** prima di usarle, Claude non ha la certezza.
- Java 21 LTS — la più richiesta negli annunci; Java 25 LTS esiste (ed è già installato), ma 21 garantisce compatibilità ovunque.
- Spring Boot ultima stabile su start.spring.io (assumo 4.x), Maven — è quello che si trova in azienda.
- PostgreSQL 16+ e Flyway — standard de facto, migrazioni versionate.
- JUnit 5, AssertJ, Mockito, Testcontainers — lo stack di test che i colloqui citano.
- Spring Security resource server JWT (chiavi RSA), springdoc-openapi — standard, niente librerie esotiche.
- Spring AI 2.x (ChatClient, immagine in ingresso, output su `record`) con un modello multimodale via API; in F8 lo stesso codice su Amazon Bedrock — una feature IA concreta, non un chatbot.
- Apache Kafka 4.x (solo KRaft) + Spring for Apache Kafka, Testcontainers Kafka — un flusso event-driven con outbox, dentro il monolite.
- TypeScript, React 19, Expo ultimo SDK stabile (assumo 55+), Expo Router, TanStack Query, expo-secure-store — lo stack che i docs Expo consigliano.
- Jest + React Native Testing Library, Maestro — unit ed e2e senza dolore.
- Docker + Compose, Caddy (HTTPS automatico), GitHub Actions, GHCR, EAS — il minimo moderno completo.
- Hetzner (consigliato; prezzi da verificare in F2), Actuator/Micrometer/Prometheus/Grafana, UptimeRobot, Backblaze B2 — infra reale a pochi €/mese.
- AWS in F8: S3, IAM, Bedrock, Budgets, descritti con Terraform (provider AWS); certificazione AWS Certified Developer – Associate (DVA-C03, 150 $).
- Web: Vite + React Router su Cloudflare Pages o Netlify.
- IDE: IntelliJ IDEA Ultimate (All Products Pack) per tutto — Spring, TypeScript/React, database, HTTP Client; completamento IA multi-riga e agenti spenti sul progetto, perché il codice lo scrivo io.

## Non ora (e perché)
- Kubernetes: un Compose su un VPS è ciò che fa gran parte delle aziende medie; K8s senza un team da gestire è solo costo.
- Microservizi, Spring Cloud, Kafka Streams: un monolite modulare ben testato vale di più in un colloquio di un "sistema distribuito" che non regge. Kafka entra solo in F6, per un flusso dentro il monolite (outbox → topic → consumer idempotente): il pezzo event-driven che gli annunci chiedono, senza microservizi.
- WebFlux, GraphQL, Kotlin: ottimi, ma spostano l'attenzione dalle fondamenta che i colloqui verificano.
- Redux, Next.js, codice nativo: Query + state locale bastano; SSR non serve a una dashboard privata; il nativo è un mestiere a parte.
- Chatbot, RAG, agenti: l'IA entra come una feature concreta (scansione in F5), non come progetto a sé.
- Un secondo progetto: no. Uno, finito, in produzione.

## Ordine di taglio quando una fase sfora 1,5×
1. Terraform (F8, AWS) → risorse AWS create a mano dalla console, documentate nel runbook.
2. Prometheus/Grafana (F7) → si resta con Actuator + UptimeRobot.
3. Build iOS / Apple Developer (F6) → l'iPhone resta su Expo Go: niente build installabile e niente push remote senza i 99 $.
4. Kafka (F6) → eventi Spring interni (`@TransactionalEventListener`); l'outbox resta.
5. Push (F6) → i turni restano senza promemoria.
6. Certificazione AWS (F8) → dopo ottobre 2027; il progetto AWS resta.
Mai tagliare: dashboard web (F7), test unit/slice/integrazione (tutte le fasi; gli e2e Maestro sì), pipeline (F2), sicurezza (F4).

## Kit anti-abbandono (tarato su come mi sono fermato prima)
- **Rituale**: 3 sessioni fisse in agenda, come un corso serale. Ogni sessione chiude con due righe in `DIARIO.md` («fatto: X — prossima volta: Y»). Il costo di rientro è il motivo per cui si smette: quelle due righe lo azzerano.
- **Settimane leggere**: Natale, Pasquetta e Ferragosto sono già nel calendario come settimane da una sola sessione. Rallentare lì non è un fallimento, è il piano.
- **Margine in ogni fase**: le stime sono realistiche blocco per blocco e la capacità della fase è più alta. Finire prima è la norma, non l'eccezione.
- **Vittoria a metà fase**: ogni fase lunga ha una consegna visibile a metà (F1: l'app legge dal DB; F2: il primo deploy a mano; F3: la lista con Query; F4: il login sul telefono).
- **Metrica visibile**: test verdi, giorni in produzione, commit a settimana — badge nel README, grafico dei commit su GitHub.
- **Utenti veri**: da gennaio 2027 (fine F2) la lista la usa la mia famiglia. «Non ho un vero obiettivo» non esiste più: c'è gente che aspetta la feature.
- **Aggiornamento pubblico mensile**: 3 righe (README o LinkedIn) su cosa funziona e cosa ho imparato. 10 minuti, e serve anche al personal branding.
- **Regola 1,5×**: se sforo, si taglia scope. Il taglio è previsto nel piano, non è un fallimento.
- **Feynman con limite**: al massimo 2 tentativi; poi si passa, con la lacuna registrata nel debito.
- **Quando sto per mollare**: non decido in sessione. 25 minuti sul task più piccolo possibile (un test, un colore). `/bloccato`. E rileggo il perché (`CLAUDE.local.md`): ogni settimana saltata è il prezzo di smettere.
- **Dal checkpoint** le domande da colloquio che incontro sono il feedback loop: ogni domanda a cui non so rispondere diventa il task della sessione dopo.
