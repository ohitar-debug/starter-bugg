from simple_bug import divide
import pytest



def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)