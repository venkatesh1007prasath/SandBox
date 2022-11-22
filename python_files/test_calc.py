from simple_calc import add
import pytest


@pytest.mark.parametrize("a,b,res", [(1, 1, 2), (2, 2, 4)])
def test_add(a, b, res):
    ret = add(a, b)
    assert ret == res
