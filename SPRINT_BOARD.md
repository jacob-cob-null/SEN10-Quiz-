# Sprint 1 — Gotham Dispatch Vertical Prototype

**Roles**
- Product Owner: represents Gotham City Council
- Scrum Master: timebox + blocker enforcement
- Dev (Backend), Dev (Frontend)

**Product Backlog** (Product Owner)
1. As a citizen, I want to submit a fire/police/medical report w/ location.
2. As a dispatcher, I want to see incoming reports in real-time.
3. As a dispatcher, I want to assign a unit to a report.
4. As a citizen, I want confirmation my report was received.
5. As a council auditor, I want reports persisted to a DB (deferred → Sprint 2).

**Sprint Goal**
Citizen submits one report type w/ location → appears on dispatcher list, dispatcher assigns unit.

---

## Kanban Board

| To Do | In Progress | Done |
|---|---|---|
| Story 5: DB persistence | — | Story 1: Citizen report form (HTML) |
| Story 4: SMS/email confirmation | — | Story 1: POST /api/reports backend route |
| Multi-unit auto-dispatch logic | — | Story 2: Dispatcher list view (HTML) |
| Auth/login for dispatchers | — | Story 2: GET /api/reports + 3s polling |
| Map/geolocation pin | — | Story 3: Assign unit dropdown + POST /assign |
| | | Story 3: /api/units/<type> lookup |
| | | Define JSON payload schema |
| | | Smoke test: submit → list → assign |

**Definition of Done (met):** code runs w/o crashing; citizen can submit; dispatcher sees it; unit can be assigned.
