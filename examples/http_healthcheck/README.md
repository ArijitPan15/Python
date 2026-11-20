# Standard-library HTTP health checker

A self-contained Python networking/backend example using `urllib.request`,
dataclasses, monotonic timing, JSON output and dependency injection for tests.
No third-party packages are required (Python 3.10+).

## Run

```bash
python examples/http_healthcheck/healthcheck.py https://example.com --timeout 3
python examples/http_healthcheck/healthcheck.py https://example.com --expected 200
python -m unittest discover -s examples/http_healthcheck -p 'test_*.py'
```

The CLI emits a JSON array containing the URL, status, elapsed milliseconds,
health flag and any error. Exit code 0 means **all** endpoints returned the
expected status; exit code 1 means at least one did not. Invalid CLI arguments
exit with argparse's code 2.

## Design notes

- Requests use GET (rather than HEAD) because many application endpoints do
  not implement HEAD consistently.
- HTTP error responses retain their status code for diagnostics.
- Network errors produce `null` status and a readable error.
- The timing includes the request/response-header exchange, not downloading
  the full response body. This is not a load-testing tool.
- Tests inject fake openers and never access the network.
- Use only trusted endpoint URLs; this utility does not restrict internal
  network destinations or implement SSRF protections.
