# COLLOQUIO — banca domande

Usata da `/colloquio`. Formato: `- [Fx][tema] Domanda` · temi: spring, jpa, security, testing, react, devops, progetto, java, http, sql, git, design, js, ts, web, soft, kafka, ai, aws.
Entrano in gioco le domande delle fasi chiuse più quella corrente (vedi STATO). Le domande incontrate fuori di qui vanno in fondo, senza date né aziende (il repo è pubblico: i dettagli stanno in `studio/registro.privato.md`).

## F0
- [F0][spring] Cosa fa `@SpringBootApplication` e cos'è l'auto-configurazione?
- [F0][spring] Cos'è uno starter? Cosa c'è dentro `spring-boot-starter-webmvc` (in Boot 3: `spring-boot-starter-web`)?
- [F0][java] Cosa usi davvero di Java 17/21 rispetto a Java 8: record, `var`, switch expression, text block, virtual thread (cosa sono, non la storia).
- [F0][java] Contratto di `equals` e `hashCode`: cosa succede in una `HashMap` se lo rompi.
- [F0][java] `ArrayList` vs `LinkedList`; `HashMap` vs `TreeMap`: quando scegli quale.
- [F0][java] Immutabilità: `final`, `record`, collezioni immutabili; perché conviene.
- [F0][java] Eccezioni checked vs unchecked: quando usi le une e le altre.
- [F0][java] Generics: cos'è la type erasure; `? extends` vs `? super`.
- [F0][java] Stream: `map` vs `flatMap`, operazioni lazy e terminali; quando non usare `Optional`.
- [F0][java] Heap e stack; cosa fa il garbage collector, in due righe.
- [F0][progetto] Perché un monorepo? Cosa cambieresti con un team di 5?

## F1
- [F1][spring] Spring vs Spring Boot: cosa aggiunge Boot.
- [F1][spring] Cos'è l'IoC container; `ApplicationContext` e cosa fa all'avvio.
- [F1][spring] `@Component` vs `@Bean`; come risolve due bean dello stesso tipo (`@Qualifier`, `@Primary`).
- [F1][spring] Come funziona l'auto-configurazione: `@Conditional…`, starter, override con un bean mio.
- [F1][spring] Constructor injection vs field injection: perché la prima.
- [F1][spring] Ciclo di vita di un bean; scope singleton e prototype.
- [F1][spring] Cosa fa `@Transactional`, come funziona il proxy (JDK vs CGLIB), su quali eccezioni fa rollback di default.
- [F1][spring] Il percorso di una richiesta nel `DispatcherServlet`, dal filtro al controller e ritorno.
- [F1][spring] `@Controller` vs `@RestController`; cosa fa `@ResponseBody`.
- [F1][spring] Come gestisci gli errori in una REST API Spring (`ProblemDetail`, `@RestControllerAdvice`).
- [F1][spring] Profili e configurazione: `@Value` vs `@ConfigurationProperties`; come configuri local/test/prod.
- [F1][jpa] Differenza tra JPA, Hibernate e Spring Data JPA.
- [F1][jpa] Stati di un'entità (transient, managed, detached, removed) e cosa fanno `persist` vs `merge`.
- [F1][jpa] Perché Flyway e non `ddl-auto=update` in produzione.
- [F1][testing] `@WebMvcTest` vs `@DataJpaTest` vs `@SpringBootTest`: cosa carica ciascuno e quando usarlo.
- [F1][testing] Cos'è Testcontainers e perché è meglio di H2 per i test di integrazione.
- [F1][testing] Mock, stub e spy: differenze, con un esempio dei tuoi test.
- [F1][java] `ExecutorService` e `CompletableFuture`: come esegui due chiamate in parallelo e combini il risultato.
- [F1][java] `synchronized` vs `volatile`; cos'è una race condition.
- [F1][http] Metodi sicuri e idempotenti; PUT vs PATCH; cosa succede se ripeti un POST.
- [F1][http] Quale status code per: creato, nessun contenuto, input invalido, non autenticato, vietato, non trovato, conflitto.
- [F1][http] Cosa vuol dire che un'API REST è stateless; come versioni e pagini un'API.
- [F1][sql] INNER vs LEFT JOIN; GROUP BY con HAVING: un esempio sul tuo schema.
- [F1][sql] Cos'è un indice, quando non aiuta, perché conta l'ordine delle colonne in un indice composto; come leggi un `EXPLAIN`.
- [F1][sql] ACID e livelli di isolamento: cosa sono dirty read e phantom read.

## F2
- [F2][devops] Cosa fa la tua pipeline, passo per passo. Cosa succede se un test fallisce.
- [F2][devops] Immagine vs container; cosa sono i layer; perché un Dockerfile multi-stage.
- [F2][devops] Come gestisci i segreti in CI e in produzione.
- [F2][devops] Cosa fa un reverse proxy; come ottieni HTTPS.
- [F2][git] Merge vs rebase; come risolvi un conflitto; trunk-based vs GitFlow.
- [F2][design] Monolite modulare vs microservizi: quando divideresti FamilyHub e cosa perderesti.
- [F2][design] API gateway, circuit breaker, service discovery: cosa sono, a parole (non li usi, ma te li chiedono).
- [F2][devops] Kubernetes in cinque concetti: pod, deployment, service, ingress, config/secret.
- [F2][progetto] Perché Compose su un VPS e non Kubernetes?
- [F2][progetto] Raccontami un bug difficile che hai risolto in questo progetto.
- [F2][progetto] Una decisione tecnica che rifaresti diversamente e perché.

## F3
- [F3][react] Cos'è un componente, cosa sono props e state, perché lo state è immutabile.
- [F3][react] Cosa fa `useEffect`; come faresti un fetch con `useEffect` (cleanup, race condition) e cosa risolve TanStack Query.
- [F3][react] Cosa sono le `key` in una lista e cosa succede se usi l'indice.
- [F3][react] Cosa causa un re-render; quando servono davvero `useMemo` e `useCallback`.
- [F3][react] Input controllati vs non controllati.
- [F3][react] Come funziona una mutazione ottimistica con TanStack Query.
- [F3][react] Differenza tra React e React Native; cos'è Expo.
- [F3][js] Cos'è una closure; come funziona `this` in una funzione normale e in una freccia.
- [F3][js] Event loop: perché un `setTimeout(…, 0)` gira dopo una Promise risolta.
- [F3][js] `==` vs `===`; `let`, `const` e `var`.
- [F3][ts] `type` vs `interface`; union e narrowing; `unknown` vs `any`.
- [F3][ts] Generics in TypeScript vs Java: cosa cambia con la tipizzazione strutturale.
- [F3][testing] Cosa testi di un componente e cosa no.

## F4
- [F4][security] Filter chain di Spring Security: cosa succede a una richiesta con Bearer token.
- [F4][security] Com'è fatto un JWT (header, payload, firma); cosa non ci metti mai.
- [F4][security] Access token vs refresh token; perché due; dove li salvi su mobile.
- [F4][security] CORS e CSRF: cosa sono, perché il CSRF non serve con Bearer stateless.
- [F4][security] Perché BCrypt e non SHA-256 per le password.
- [F4][security] Come garantisci che un utente non veda i dati di un'altra famiglia? Come lo testi?
- [F4][soft] Parlami di te in due minuti (perché da Java EE a Spring e React).
- [F4][soft] Perché cambi lavoro? Cosa cerchi nel prossimo team?
- [F4][soft] Raccontami un conflitto in un team e come l'hai gestito.
- [F4][soft] Come lavori in Scrum: cerimonie, stime, cosa fai quando una stima salta.
- [F4][soft] Qual è la tua RAL attesa, e come ci sei arrivato?

## F5
- [F5][jpa] Cos'è il problema N+1, come lo rilevi, tre soluzioni.
- [F5][jpa] Lazy vs eager; `LazyInitializationException`: perché succede e come la eviti.
- [F5][jpa] Locking ottimistico (`@Version`) vs pessimistico.
- [F5][jpa] Projection e DTO nelle query: perché non restituire entità.
- [F5][spring] Propagazione delle transazioni: `REQUIRED` vs `REQUIRES_NEW`; perché `@Transactional` su un metodo chiamato dalla stessa classe non funziona.
- [F5][spring] Cosa esponi con Actuator e come lo proteggi.
- [F5][java] Lombok e MapStruct: cosa fanno, pro e contro; perché `@Data` su un'entità JPA è pericoloso.
- [F5][ai] Come estrai dati strutturati da una foto con Spring AI? Cosa fai se il modello risponde male o inventa?
- [F5][ai] Come testi codice che chiama un modello IA, senza chiamarlo in CI?
- [F5][ai] Costi, privacy e chiavi API: cosa hai deciso per la scansione degli scontrini e perché?

## F6
- [F6][progetto] Come funzionano le push nella tua app, end-to-end. Come eviti i doppioni dello scheduler?
- [F6][devops] EAS Build vs EAS Update; cosa puoi aggiornare OTA e cosa no.
- [F6][kafka] Topic, partizione, offset, consumer group: cosa sono e come li usi nel tuo flusso.
- [F6][kafka] Cos'è il pattern outbox e quale problema risolve (la doppia scrittura DB + broker).
- [F6][kafka] At-least-once vs exactly-once; come rendi idempotente un consumer.
- [F6][kafka] Perché Kafka e non una tabella-coda o RabbitMQ, nel tuo caso? Cosa ci perdi?
- [F6][kafka] Cosa succede se il consumer è giù per un'ora? E se un messaggio fallisce sempre?

## F7
- [F7][web] Flex vs grid; come rendi accessibile un form.
- [F7][web] Dove tieni il token nella dashboard web: memoria, localStorage o cookie httpOnly? Cosa cambia per XSS e CSRF.
- [F7][devops] Cos'è il lag di un consumer Kafka e perché lo monitori.
- [F7][devops] Quali metriche guardi per capire se l'API sta bene. Cos'è p95.
- [F7][devops] Come fai backup e come sai che funziona.
- [F7][design] Cache, scalabilità orizzontale, pool di connessioni: cosa toccheresti per primo con 10× utenti.
- [F7][progetto] Dove si rompe per primo il tuo sistema con 10× utenti? Cosa faresti?

## F8
- [F8][aws] IAM: utente, ruolo, policy; come applichi il privilegio minimo nel tuo progetto.
- [F8][aws] Come carichi un file su S3 dall'app senza farlo passare dal backend? Rischi degli URL presigned.
- [F8][aws] Modello di responsabilità condivisa: cosa resta a te, cosa ad AWS.
- [F8][aws] Bedrock o API diretta del provider: cosa cambia (costi, dati, regione, IAM)?
- [F8][devops] Cos'è lo stato di Terraform e perché conta. `plan` vs `apply`.

## Raccolte fuori di qui
(aggiungi qui: `- [extra][tema] Domanda · come è andata` — senza date né aziende)
