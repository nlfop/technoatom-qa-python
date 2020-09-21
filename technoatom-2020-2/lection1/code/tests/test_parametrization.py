import pytest


@pytest.mark.parametrize('i', list(range(10)))
def test(i):
    """
    :param i: integer from 0 to 9
    :return:
    """
    assert i % 2 == 0
