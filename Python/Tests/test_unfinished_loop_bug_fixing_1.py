from Python.unfinished_loop_bug_fixing_1 import create_array
import pytest


@pytest.mark.parametrize('num, answer', [(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])])
def test_solution(num, answer):
    assert create_array(num) == answer
