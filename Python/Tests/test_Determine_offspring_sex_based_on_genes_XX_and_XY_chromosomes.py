import pytest

from Python.determine_offspring_sex_based_on_genes_XX_and_XY_chromosomes import chromosome_check


@pytest.mark.parametrize("data, result", [('XX', 'Congratulations! You\'re going to have a daughter.'),
                                           ('XY', 'Congratulations! You\'re going to have a son.')])
def test_compairation(data, result):
    assert chromosome_check(data) == result
