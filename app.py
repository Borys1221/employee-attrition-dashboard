from __future__ import annotations

import argparse
import http.server
import socketserver
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_PORT = 8765


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return


def validate_project() -> None:
    required_files = ["index.html", "dashboard.html", "hr_clean.csv"]
    missing = [name for name in required_files if not (PROJECT_ROOT / name).exists()]
    if missing:
        missing_text = ", ".join(missing)
        raise FileNotFoundError(f"Missing required project files: {missing_text}")


def serve(port: int) -> None:
    validate_project()
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(PROJECT_ROOT), **kwargs)
    with socketserver.TCPServer(("127.0.0.1", port), handler) as server:
        print(f"Dashboard: http://127.0.0.1:{port}/index.html")
        print("Press Ctrl+C to stop.")
        server.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Employee Attrition dashboard locally.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Local server port.")
    args = parser.parse_args()
    serve(args.port)


if __name__ == "__main__":
    main()
