# test_f2.py
import pytest


@pytest.fixture()
def user():
    print("Get user name")
    a = 'jingo'
    b = '12356'
    return (a, b)


def test_1(user):
    u = user[0]
    p = user[1]
    print("Test user: %s, password: %s" % (u, p))
    assert u == 'jingo'


if __name__ == '__main__':
    pytest.main(['-s', 'test_f2.py'])
