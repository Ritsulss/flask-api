# Agile Project Record

This project is run as one Scrum-style sprint. Replace every `[bracketed]` field with your own details.

- **Product owner / developer:** [your name]
- **Sprint:** 1
- **Dates:** [start date] to [end date]
- **Sprint goal:** Deliver a tested Flask API that returns JSON from `/hello` and `/data`, ready to build on in Project 2.

## Product backlog

Story points use the scale 1, 2, 3, 5.

| ID   | User story                                                                                  | Priority | Points | Status |
| ---- | ------------------------------------------------------------------------------------------- | -------- | ------ | ------ |
| US-1 | As an API user, I want `GET /hello` to return a welcome message so I know the API is running. | Must     | 1      | Done   |
| US-2 | As an API user, I want `POST /hello` to greet me by name so I can confirm my input was received. | Must     | 2      | Done   |
| US-3 | As an API user, I want `GET /data` to return structured sample data so I can use it in a client. | Must     | 1      | Done   |
| US-4 | As an API user, I want `POST /data` to add an item so I can submit new data.                | Must     | 3      | Done   |
| US-5 | As an API user, I want clear JSON errors so I can fix bad requests.                         | Should   | 2      | Done   |
| US-6 | As a developer, I want automated tests so I can change the code safely.                     | Must     | 3      | Done   |
| US-7 | As a reviewer, I want a README and evidence of working calls so I can verify the project.   | Must     | 2      | Done   |
| US-8 | As an API user, I want data saved in a database so it survives a restart.                   | Could    | 5      | Later  |

## Acceptance criteria

| ID   | Criteria                                                                                     | Verified by              |
| ---- | -------------------------------------------------------------------------------------------- | ------------------------ |
| US-1 | Returns 200 and a JSON `message`.                                                            | pytest, demo script      |
| US-2 | Returns 200 with the name in the greeting. A missing or blank name returns 400.              | pytest, demo script      |
| US-3 | Returns 200 with `count` and a list of `items`.                                              | pytest, demo script      |
| US-4 | Returns 201 with the new item and its `id`. The item then appears in `GET /data`.            | pytest, demo script      |
| US-5 | Bad input returns 400. Unknown routes return 404. Unsupported methods return 405. All are JSON. | pytest                |
| US-6 | Every endpoint has success and failure tests, and the whole suite passes.                    | pytest                   |
| US-7 | README covers setup, running, and endpoints. Screenshots show JSON responses.                | Review                   |

## Definition of Done

A story is done when:

1. Its acceptance criteria are met.
2. Its automated tests pass.
3. The change is committed to GitHub with its story ID in the commit message, such as `US-1: Add GET /hello`.
4. The README is updated if behavior changed.

## Sprint plan

**Sprint 1 scope:** US-1 to US-7, 14 story points.

**Moved out of scope:** US-8. An in-memory list is enough for this assignment, and persistence can be planned with Project 2.

## Task board

Mirror this table in a GitHub Project board with To Do, In Progress, and Done columns.

| To Do | In Progress | Done                                               |
| ----- | ----------- | -------------------------------------------------- |
| US-8  |             | US-1, US-2, US-3, US-4, US-5, US-6, US-7           |

## Daily scrum log

Add one row for each work session. For a solo project, this is a short self-check.

| Date   | Done since last session | Plan for this session | Blockers |
| ------ | ----------------------- | --------------------- | -------- |
| [date] | [notes]                 | [notes]               | [notes]  |

## Sprint review

| Measure                 | Result |
| ----------------------- | ------ |
| Story points planned    | 14     |
| Story points completed  | 14     |
| Demo evidence           | `docs/evidence/` |
| Demo date               | [date] |
| Feedback received       | [notes] |

## Sprint retrospective

- **What went well:** [your notes]
- **What could improve:** [your notes]
- **One change for the next sprint:** [your notes]
