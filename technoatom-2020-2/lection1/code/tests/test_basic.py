import pytest


def test_dnfmnsdfbnmsdf():
    assert 1 == 1


class TestClass:

    def test1(self):
        assert 1 != 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            assert 1 / 0
