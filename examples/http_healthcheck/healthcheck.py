"""Small dependency-free HTTP health checker for scripts and CI."""
from __future__ import annotations

import argparse
import json
import time
from dataclasses import asdict, dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class CheckResult:
    url: str
    healthy: bool
    status: int | None
    elapsed_ms: float
    error: str | None = None


def check_url(url: str, *, timeout: float = 5.0, expected: int = 200,
              opener=urlopen, clock=time.monotonic) -> CheckResult:
    """Perform one GET request; HTTP error responses retain their status."""
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    if not 100 <= expected <= 599:
        raise ValueError("expected status must be between 100 and 599")

    started = clock()
    status = None
    error = None
    try:
        request = Request(url, headers={"User-Agent": "stdlib-healthcheck/1.0"})
        with opener(request, timeout=timeout) as response:
            status = response.status
    except HTTPError as failure:
        status = failure.code
        error = str(failure)
        failure.close()
    except (URLError, TimeoutError, OSError) as failure:
        error = str(failure)
    elapsed = round((clock() - started) * 1000, 2)
    return CheckResult(url, status == expected, status, elapsed, error)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check HTTP endpoint health")
    parser.add_argument("urls", nargs="+", help="HTTP(S) endpoints")
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--expected", type=int, default=200)
    arguments = parser.parse_args(argv)
    if arguments.timeout <= 0 or not 100 <= arguments.expected <= 599:
        parser.error("timeout must be positive and expected status must be 100-599")
    outcomes = [
        check_url(url, timeout=arguments.timeout, expected=arguments.expected)
        for url in arguments.urls
    ]
    print(json.dumps([asdict(outcome) for outcome in outcomes], indent=2))
    return 0 if all(outcome.healthy for outcome in outcomes) else 1


if __name__ == "__main__":
    raise SystemExit(main())
