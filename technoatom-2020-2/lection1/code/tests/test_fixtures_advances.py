import os
import random

import pytest


@pytest.fixture(autouse=True)
def new_file(random_file_name):
    print('123')
    f = open(random_file_name, 'w')
    yield f
    f.close()
    os.remove(random_file_name)


@pytest.fixture(scope='session')
def random_file_name():
    return str(random.randint(1, 100))


def fdsklfsdklf():
    pass
