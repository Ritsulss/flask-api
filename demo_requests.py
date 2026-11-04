"""Call every endpoint on a running server and print the JSON responses.

Start the server first with `python app.py`, then run `python demo_requests.py`.
Exits with status 1 if a response has an unexpected status code.
"""

import json
import sys

import requests

BASE_URL = "http://127.0.0.1:5000"

CALLS = [
    ("GET", "/hello", None, 200),
    ("POST", "/hello", {"name": "Student"}, 200),
    ("GET", "/data", None, 200),
    ("POST", "/data", {"name": "Headphones", "category": "electronics"}, 201),
    ("GET", "/data", None, 200),
    ("POST", "/data", {"name": "Headphones"}, 400),
]


def main():
    failures = 0
    for method, path, body, expected in CALLS:
        try:
            response = requests.request(method, BASE_URL + path, json=body, timeout=5)
        except requests.ConnectionError:
            print(f"Could not reach {BASE_URL}. Start the server with: python app.py")
            return 1

        passed = response.status_code == expected
        failures += not passed
        print(f"{method} {path}")
        if body is not None:
            print(f"Request:  {json.dumps(body)}")
        print(f"Status:   {response.status_code} (expected {expected})")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print("-" * 60)

    print(f"{len(CALLS) - failures}/{len(CALLS)} calls returned the expected status.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
