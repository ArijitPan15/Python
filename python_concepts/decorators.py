"""Reusable decorators with preserved function metadata."""
from functools import wraps
from time import perf_counter


def repeat(times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("times must be a nonnegative integer")
    def decorate(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(function(*args, **kwargs))
            return results
        return wrapper
    return decorate


def count_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return function(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def timed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            wrapper.last_elapsed = perf_counter() - start
    wrapper.last_elapsed = None
    return wrapper
