import pytest

from myapp.app import multiply_by_two, divide_by_two, area_of_square


@pytest.fixture
def square_mumbers():
    a = 38
    b = 1444
    return [a,b]

@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:


    def test_square_area(self,square_mumbers):
        res = area_of_square(square_mumbers[0])
        assert res == square_mumbers[1]
        
    def test_square_area_fail(self,square_mumbers):
        res = square_mumbers[1] # Now the faileed test should pass 
        assert res == area_of_square(square_mumbers[0])

    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]
    
   
