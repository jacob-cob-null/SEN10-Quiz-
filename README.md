# Gotham Emergency Services Dispatch System

## Project Purpose

The Gotham City Council has contracted the team to build a next-generation Emergency Services Dispatch System for Gotham. The system must let citizens report emergencies through a web portal and let dispatchers see those reports in near real-time so they can assign units based on location.

This project is intentionally scoped as an evolutionary vertical prototype. The goal is not to build the entire final product in one sprint. The goal is to deliver one working end-to-end slice of the core reporting flow so the Product Owner can inspect a real implementation, provide feedback, and re-prioritize the backlog.

## Why Scrum Instead of Waterfall

The requirements are volatile, the stakeholders are difficult to reach, and the product will likely change after every demo. A traditional Waterfall approach would lock the team into assumptions too early and would not adapt quickly enough to feedback from the Council.

Scrum is the correct framework because it:

- Supports short feedback loops.
- Lets the team ship a usable increment by the end of the sprint.
- Makes uncertainty visible through the Product Backlog.
- Encourages inspection and adaptation at the Sprint Review and Retrospective.
- Keeps the team focused on one Sprint Goal instead of trying to build every feature at once.

## Product Vision

Citizens should be able to:

- Open the citizen portal.
- Select an emergency type: Fire, Police, or Medical.
- Enter a location.
- Optionally include a brief description.
- Submit the report successfully.

Dispatchers should be able to:

- Open a dispatcher dashboard.
- See incoming reports as they are submitted.
- Review the emergency type, location, timestamp, and status.
- Assign an available unit to the report.

For Sprint 1, the target is a vertical prototype that proves the full reporting path from citizen input to dispatcher assignment.

## Current Repository Snapshot

The existing workspace already contains the core prototype pieces:

- [app.py](app.py) contains the Flask backend.
- [templates/citizen.html](templates/citizen.html) contains the citizen-facing page.
- [templates/dispatcher.html](templates/dispatcher.html) contains the dispatcher-facing page.
- [SPRINT_BOARD.md](SPRINT_BOARD.md) contains a concise sprint backlog snapshot.
- [RETRO.md](RETRO.md) contains the sprint review and retrospective notes.

The current backend already includes:

- A citizen portal route.
- A dispatcher view route.
- A POST endpoint for submitting reports.
- A GET endpoint for listing reports.
- An assign-unit endpoint.
- A unit lookup endpoint by emergency type.

## Phase 1: Scrum Initialization & Sprint Planning

### 1. Role Assignment

Assign the team roles before coding starts.

#### Product Owner

The Product Owner represents the Gotham City Council. This person owns the Product Backlog, writes the user stories, and defines what value matters most for this sprint.

Responsibilities:

- Capture stakeholder needs.
- Clarify the highest-value user stories.
- Decide which stories are most important for Sprint 1.
- Review the prototype during Sprint Review.
- Update or add backlog items based on feedback.

#### Scrum Master

The Scrum Master manages the Scrum process and protects the team from losing focus.

Responsibilities:

- Timebox planning, development, daily scrum, review, and retrospective.
- Keep the team aligned on the Sprint Goal.
- Remove blockers when possible.
- Make sure Scrum rules are followed.
- Prevent scope creep during the sprint.

#### Development Team

The remaining team members are the Development Team.

Typical split:

- One frontend developer.
- One backend developer.

Responsibilities:

- Design and implement the prototype.
- Break stories into technical tasks.
- Collaborate on integration.
- Ensure the increment works end to end.
- Maintain the Kanban board.

### 2. Product Backlog Creation

The Product Owner should capture 4 to 5 high-level user stories.

Suggested Product Backlog:

1. As a citizen, I want to submit a fire, police, or medical report with my location so that emergency services can respond.
2. As a dispatcher, I want to see incoming reports in real time so that I can prioritize active emergencies.
3. As a dispatcher, I want to assign a unit to a report so that the proper response team is dispatched.
4. As a citizen, I want confirmation that my report was received so that I know the system accepted it.
5. As a council auditor, I want reports persisted in storage so that emergency records are not lost after a restart.

Recommended ordering for Sprint 1:

- Story 1 must be included.
- Story 2 should be included if the team can still finish a working prototype.
- Story 3 is a natural extension of the same flow and should also be included if possible.
- Stories 4 and 5 can remain in the backlog if they threaten the sprint goal.

### 3. Sprint Planning

The team should agree on a Sprint Goal before any implementation begins.

#### Example Sprint Goal

Deliver a vertical prototype where a citizen can submit one type of emergency report with a location and the report appears on a dispatcher list where a unit can be assigned.

#### Planning Outcome

The Development Team should choose the top 1 to 2 backlog items and break them into tasks.

Example task breakdown:

- Create the citizen HTML form.
- Create the Flask route that serves the citizen portal.
- Build the JSON payload for report submission.
- Create the backend POST endpoint for new reports.
- Create the dispatcher dashboard.
- Create the GET endpoint for retrieving all reports.
- Add polling or refresh behavior to update the dispatcher view.
- Add the unit assignment control and assign endpoint.
- Define the unit list by emergency type.
- Validate the end-to-end flow with a smoke test.

#### Kanban Board Structure

Use a simple board with three columns:

- To Do
- In Progress
- Done

The board should show the smallest useful tasks rather than giant abstract features.

### 4. Sprint Planning Deliverables

By the end of planning, the team should have:

- Assigned roles.
- A prioritized Product Backlog.
- A clear Sprint Goal.
- A selected Sprint Backlog.
- A visible Kanban board.

## Phase 2: Sprint Execution

### 1. Development Window

During development, the team should only work on the sprint goal.

The working prototype should include:

- A functional citizen portal.
- A backend route to accept a report.
- A dispatcher dashboard.
- A mechanism for the dispatcher to view incoming reports.
- A mechanism to assign a response unit.

The prototype can be minimal, but it must run without crashing and show a complete vertical slice.

### 2. Definition of Done

For this sprint, a story is done when:

- The code runs locally or through a working hosted link.
- The feature does not crash during normal use.
- The citizen can submit a valid report.
- The dispatcher can see the report.
- The dispatcher can assign a unit.
- The team can demonstrate the flow to the Product Owner.

### 3. Daily Scrum

Pause development for the Daily Scrum.

Each developer answers three questions:

1. What did I complete since the last scrum?
2. What am I working on next?
3. What is blocking me?

The Scrum Master should record impediments and help resolve them quickly.

#### Common impediments in this project

- A route is not returning the expected data.
- Frontend and backend data shapes do not match.
- The dispatcher list is not refreshing.
- The server crashes on bad input.
- The team is spending time on extra features instead of the sprint goal.

### 4. Development Resumes

After the Daily Scrum, the team returns to implementation and finishes the prototype.

The team should verify that:

- The citizen form submits the correct data.
- The backend accepts the report.
- The dispatcher view can display multiple reports.
- A unit can be assigned successfully.
- The prototype remains stable during demonstration.

## Phase 3: Inspection, Adaptation & Submission

### 1. Sprint Review

The Development Team demonstrates the working prototype to the Product Owner.

The Product Owner inspects the software and provides immediate feedback.

Potential review feedback items:

- The system needs visible confirmation after report submission.
- The dispatcher dashboard needs clearer status labeling.
- Reports should be persisted so they do not vanish after restart.
- The interface should better support future real-time updates.
- More emergency types or richer triage logic may be needed later.

The Product Owner then updates the Product Backlog based on what was learned during the demo.

### 2. Sprint Retrospective

The entire Scrum Team reflects on the sprint process.

Discussion prompts:

- What went well?
- What did not go well?
- What slowed the team down?
- Which tools or communication patterns helped?
- What should be changed in the next sprint?

Possible retrospective outcomes:

- Keep the vertical slice approach because it produces a demoable increment quickly.
- Add a checkpoint for known limitations during planning.
- Improve handoff between frontend and backend tasks.
- Reserve time for integration and testing before the demo.
- Re-prioritize persistence before adding new cosmetic features.

### 3. Submission Preparation

Prepare the required deliverables for grading or review.

#### Deliverable 1: Sprint Backlog Screenshot

Submit a screenshot of the final Kanban board showing tasks in:

- To Do
- In Progress
- Done

The screenshot should show the work breakdown for the vertical prototype.

#### Deliverable 2: Prototype Code or Working Link

Submit one of the following:

- The minimal frontend and backend source code for the prototype.
- A working hosted link to the running prototype.

If a working link is submitted, it should let a reviewer access the citizen portal and dispatcher page without needing to rebuild the project.

#### Deliverable 3: Retrospective Summary

Submit a brief summary of the Sprint Review feedback and the Retrospective improvements.

Expected summary content:

- What the Product Owner approved.
- What gaps or missing features the Product Owner identified.
- What the team learned during the sprint.
- What process changes the team will make next sprint.

## Recommended Technical Scope For Sprint 1

The Sprint 1 prototype should stay intentionally small.

Recommended included features:

- Citizen form with emergency type and location.
- Backend POST route to create a report.
- Dispatcher page with a report list.
- Backend GET route to fetch reports.
- Unit assignment control.
- Emergency type to unit mapping.

Recommended deferred features:

- Authentication.
- Database persistence.
- SMS alerts.
- Geolocation map integration.
- Multi-agency routing.
- Advanced analytics.
- Role-based permissions.

## Acceptance Criteria For The Vertical Prototype

The prototype satisfies Sprint 1 when all of the following are true:

- A citizen can submit a Fire, Police, or Medical report.
- The report includes a location.
- The report appears on the dispatcher side.
- The dispatcher can assign a unit.
- The application runs without crashing.
- The team can demo the workflow end to end.

## Suggested Story-to-Task Mapping

Story 1: Citizen report submission

- Build the HTML form.
- Validate the selected emergency type.
- Validate that location is present.
- Send the report to the backend API.

Story 2: Dispatcher visibility

- Build the dispatcher page.
- Add a polling mechanism or refresh logic.
- Render report cards or rows.
- Display report status.

Story 3: Unit assignment

- Add a dropdown of units based on emergency type.
- Create the assign endpoint.
- Update the report status after assignment.
- Show the assigned unit in the UI.

Story 4: Confirmation

- Add a visible success message.
- Make the feedback obvious in the citizen portal.

Story 5: Persistence

- Add a database or file-based storage layer.
- Replace in-memory storage.
- Preserve reports across restarts.

## Current Code Alignment Notes

The current backend implementation already aligns with the sprint goal in a lightweight way.

Observed alignment:

- The Flask app is already serving the citizen and dispatcher pages.
- Report data is captured through a POST API.
- Reports can be fetched through a GET API.
- Unit assignment is supported through an assign endpoint.
- Units are separated by emergency type.

Known limitations:

- Reports are stored only in memory.
- Restarting the server clears all data.
- Real-time updates are approximated through polling rather than push-based updates.
- The prototype is intentionally minimal and does not yet solve every Council concern.

## Retrospective Summary Template

Use this template when writing the required 3 to 4 sentence retrospective summary.

Template:

The Product Owner approved the end-to-end reporting flow from citizen submission to dispatcher assignment, but requested improvements to confirmation and persistence. The team successfully delivered a working vertical prototype within the sprint timebox and used a simple polling approach to keep the dispatcher list current. The main issue was that in-memory storage caused reports to disappear after restart, which should have been called out earlier as a risk. In the next sprint, the team will prioritize persistence, strengthen integration checks, and reserve time for demo hardening before review.

## Final Sprint Checklist

Before closing the sprint, confirm the following:

- The backlog is updated.
- The Kanban board is current.
- The prototype can be demonstrated.
- The submission screenshot has been captured.
- The retrospective summary has been written.
- The code or hosted link is ready for submission.

## Optional Notes For Presenters

If you are presenting this project live, keep the demo simple and stay inside the sprint goal.

Suggested demo order:

1. Open the citizen portal.
2. Submit a report.
3. Open the dispatcher page.
4. Show the report appearing in the list.
5. Assign a unit.
6. Explain what is intentionally not built yet.

That presentation style makes the increment easy to understand and keeps the conversation focused on delivered value rather than unfinished future work.