"""This module contains tests for the calculator functions."""
from calculator import add, subtract

def test_add():
    """Test addition function."""
    assert add(10, 5) == 15, "Should be 15"

def test_subtract():
    """Test subtraction function."""
    assert subtract(10, 5) == 5, "Should be 5"
