from funciones import repetidos
import pytest

def test_repetidos():
    assert repetidos([1, 2, 3, 1]) == True
    assert repetidos([1, 2, 3]) == False


@pytest.mark.parametrize("nums, res",
                         [([1, 2, 3, 1], True),
                          ([1, 2, 3], False),
                          ([1,3,3,4], True)
                          ])
def test_repetidos_parametrizado(nums, res):
    assert repetidos(nums) == res