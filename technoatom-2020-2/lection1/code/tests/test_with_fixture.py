import random


import pytest


@pytest.fixture()
def random_value():
    print('entering')
    yield random.randint(1, 1000)
    print('exiting')


def test(random_value):
    print(random_value)
    assert random_value < 50


def test1(random_value):
    print(random_value)
    assert random_value < 50


def test2(random_value):
    print(random_value)
    assert random_value < 50
