# Sprint Review & Retrospective

**Sprint Review — Product Owner Feedback**
PO approved core flow (submit → dispatcher list → assign unit) but flagged 2 gaps discovered live: no confirmation shown to citizen beyond a status banner (wants SMS eventually), and no persistence — restarting the server wipes all reports, unacceptable for council audit trail. Both added to backlog for Sprint 2, prioritized above new features.

**Retrospective**
*Went well:* vertical slice (form → API → live list → assign) delivered end-to-end within timebox; polling was a fast, "good enough" stand-in for real-time. *Went poorly:* in-memory storage was a silent scope gap not caught until demo — should've been called out as a risk during Sprint Planning. *Next Sprint:* add a 5-min "known limitations" check during planning, and pull Story 5 (DB persistence) to the top of next Sprint Backlog.
