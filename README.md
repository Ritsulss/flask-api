# Flask API Demo

A minimal Flask REST API with two JSON endpoints, automated tests, and a live demo script. It is the backend foundation for Project 2.

## Structure

```text
app.py                 Flask app and routes
demo_requests.py       Calls every endpoint on a running server
requirements.txt       Pinned dependencies
tests/test_api.py      Automated pytest suite
postman/               Postman collection (import into Postman)
docs/AGILE.md          Backlog, sprint plan, Definition of Done, retrospective
docs/evidence/         Screenshots of successful API calls
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

Start the server:

```bash
python app.py
```

In a second terminal, run the demo:

```bash
python demo_requests.py
```

To use Postman instead, import `postman/flask-api-demo.postman_collection.json` while the server is running.

## Test

```bash
pytest
```

## Endpoints

| Method | Path     | Request body                    | Success | Response                       |
| ------ | -------- | ------------------------------- | ------- | ------------------------------ |
| GET    | `/hello` | None                            | 200     | Welcome message                |
| POST   | `/hello` | `{"name": "Ada"}`               | 200     | Personalized greeting          |
| GET    | `/data`  | None                            | 200     | `count` and list of `items`    |
| POST   | `/data`  | `{"name": "...", "category": "..."}` | 201 | The created item with its `id` |

Invalid requests return JSON such as `{"error": "..."}` with a 400, 404, or 405 status.

Data is held in memory, so items added with POST are lost when the server restarts.
