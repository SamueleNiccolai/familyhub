---
name: ricalibra
description: Rivede il piano con i dati reali (sessioni, ore, date) — taglia scope nell'ordine previsto o aggiunge approfondimento, aggiorna file di fase, STATO e calendario. Argomento opzionale: motivo.
disable-model-invocation: true
argument-hint: [motivo]
allowed-tools: Bash(cat *) Bash(date *)
---

Motivo: $ARGUMENTS · Oggi: !`date +%F`

## Stato
!`cat "${CLAUDE_PROJECT_DIR}/studio/STATO.md"`

## Procedura
1. Confronta: sessioni fatte e ore cumulate vs stima della fase (nel file `studio/fasi/F<n>.md`) e date del calendario (STATO → Calendario e `studio/PIANO.md` → Fasi).
2. Diagnosi in 5 righe. È **lentezza** (meno ore del previsto: la vita), **difficoltà** (le ore ci sono ma il blocco non chiude) o **scope** (il blocco era troppo grande)? Chiedi se non è chiaro; le tre cause hanno rimedi diversi.
3. Se la fase supera o supererà 1,5× la stima: proponi tagli concreti, nell'ordine di PIANO.md (Terraform → Prometheus/Grafana → build iOS → Kafka → push → certificazione AWS). Mai tagliare la dashboard web, i test unit/slice/integrazione, la pipeline, la sicurezza. Gli item tagliati vanno in una sezione «Opzionale» del file di fase, non cancellati.
4. Se è in anticipo: proponi approfondimento (più test, una domanda da colloquio in più, una lettura dalla lista della fase), non feature nuove.
5. Se ha cambiato ore disponibili o obiettivo: ricalcola le date delle fasi successive (settimane × ore/settimana, settimane leggere comprese) e aggiorna il calendario in STATO e in PIANO.md.
6. Scrivi le modifiche: file di fase, STATO (scostamento, calendario, eventuale nota nel debito), una riga in `studio/DIARIO.md` che inizia con `ricalibrato:`. Non cambiare l'ordine delle fasi senza spiegare perché; non aggiungere fasi.

Chiudi con il nuovo prossimo passo in una riga.
