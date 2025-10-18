import pytest

from myapp.mymodule.funcs import area_of_square 


@pytest.mark.parametrize("a, b", [(38,1444),(10,100), (20,400), (11,121), (38,1444)])
def test_area_of_square(a, b):
    res = area_of_square(a)
    assert res == b
