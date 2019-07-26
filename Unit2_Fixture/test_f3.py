# test_f3.py
import pytest


@pytest.fixture()
def user():
    print("Get User")
    a = 'jingo'
    return a

@pytest.fixture()
def psw():
    print("Get Password")
    b = '123456'
    return b


def test_1(user, psw):
    '''传多个fixture'''
    print("Test User: %s, Psw: %s" % (user, psw))
    assert user == 'jingo'

if __name__ == '__main__':
    pytest.main(['-q', 'test_f3.py'])
