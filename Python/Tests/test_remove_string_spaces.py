import pytest

from Python.remove_string_spaces import no_space

@pytest.mark.parametrize("string, result", [(' das das ', 'dasdas'),
                                            ('324 sda d   ada s ', '324sdadadas')])
def test_compairation(string, result):
    assert no_space(string) == result

