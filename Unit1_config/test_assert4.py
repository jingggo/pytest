# test_assert4.py
import pytest


def is_true(a):
    if a>0:
        return True
    else:
        return False


def test_01():
    """断言xx为真"""
    a = 5
    b = -1
    assert is_true(a)
    assert not is_true(b)


def test_02():
    """断言b 包含a"""
    a = 'hello'
    b = 'hello world'
    assert a in b


def test_03():
    """断言相等"""
    a = 'yoyo'
    b = 'yoyo'
    assert a==b


def test_04():
    """断言不相等"""
    a = 5
    b = 6
    assert a != b

if __name__ == '__main__':
    pytest.main(['-s', 'test_assert4.py'])
