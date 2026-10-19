# FamilyHub

A family management app, built from scratch as a learning project with real users (my family): shared shopping list, expenses and monthly budget with AI receipt scanning, family invitations, chores and bill deadlines with event-driven push reminders, and a web dashboard.

**Stack:** Spring Boot (Java 21) · PostgreSQL · Spring AI · Kafka · React Native + Expo · React (Vite) · Docker · GitHub Actions · AWS + Terraform

**Status:** F0 of F0–F8 — environment and first end-to-end "hello list". The learning journey (in Italian) lives in [`studio/`](studio/STATO.md).

## Run
_Filled in as the project grows._

## Layout
```
backend/   Spring Boot REST API            (from phase 0)
mobile/    React Native + Expo app         (from phase 0)
web/       React dashboard                 (phase 7)
infra/     Docker Compose, Terraform       (from phase 1)
studio/    plan, state, diary, phases      (Italian)
.claude/   mentor rules, commands, hooks
```

## Working method
The code in this repository is written by me. Claude Code acts as a mentor (hints, review, verification), not as the author — see `CLAUDE.md`.
