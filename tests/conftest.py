# conftest.py
# Shared fixtures and configuration for all tests
# This file is automatically loaded by pytest before running any tests

import pytest


# Example fixture — shared setup that any test can use
@pytest.fixture
def sample_input():
    """Basic sample input fixture for testing solutions."""
    return {
        "array": [1, 2, 3, 4, 5],
        "string": "hello world",
        "number": 42,
        "nested": {"key": "value"}
    }


@pytest.fixture
def empty_input():
    """Edge case fixture — empty inputs for boundary testing."""
    return {
        "array": [],
        "string": "",
        "number": 0,
        "nested": {}
    }


@pytest.fixture
def large_input():
    """Performance fixture — larger inputs for stress testing."""
    return {
        "array": list(range(1000)),
        "string": "a" * 1000,
        "number": 999999,
    }