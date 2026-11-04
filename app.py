"""Minimal Flask JSON API with /hello and /data endpoints."""

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

SAMPLE_ITEMS = [
    {"id": 1, "name": "Laptop", "category": "electronics"},
    {"id": 2, "name": "Notebook", "category": "stationery"},
    {"id": 3, "name": "Backpack", "category": "accessories"},
]


def create_app():
    """Build the app. Each call gets its own in-memory copy of the data."""
    app = Flask(__name__)
    app.json.sort_keys = False  # keep JSON keys in the order written here
    items = [dict(item) for item in SAMPLE_ITEMS]

    @app.get("/hello")
    def get_hello():
        return jsonify(message="Welcome to the Flask API!")

    @app.post("/hello")
    def post_hello():
        body = request.get_json(silent=True)
        if not isinstance(body, dict):
            return error("Request body must be a JSON object.", 400)

        name = body.get("name")
        if not is_filled_in(name):
            return error("'name' is required and must be a non-empty string.", 400)

        return jsonify(message=f"Hello, {name.strip()}!")

    @app.get("/data")
    def get_data():
        return jsonify(count=len(items), items=items)

    @app.post("/data")
    def post_data():
        body = request.get_json(silent=True)
        if not isinstance(body, dict):
            return error("Request body must be a JSON object.", 400)

        missing = [
            field for field in ("name", "category") if not is_filled_in(body.get(field))
        ]
        if missing:
            return error(
                f"Missing or invalid field(s): {', '.join(missing)}. "
                "Each must be a non-empty string.",
                400,
            )

        item = {
            "id": max((existing["id"] for existing in items), default=0) + 1,
            "name": body["name"].strip(),
            "category": body["category"].strip(),
        }
        items.append(item)
        return jsonify(item), 201

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        """Return JSON instead of Flask's default HTML error pages."""
        return error(exc.description, exc.code)

    return app


def is_filled_in(value):
    return isinstance(value, str) and bool(value.strip())


def error(message, status):
    return jsonify(error=message), status


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
