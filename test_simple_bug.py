from simple_bug import divide
import pytest


def test_divide_ok():
    assert divide(10, 5) == 2

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)