from simple_bug import divide
import pytest

def test_divide_ok():
    assert divide(10, 2) == 5

 

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

