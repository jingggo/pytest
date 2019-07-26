# test_assert1.py
import pytest


def f():
    return 3


def test_function():
    a = f()
    assert a%2 == 0, "判断a为偶数，当前a的值为:%s"%a


if __name__ == '__main__':
    pytest.main(['-s', 'test_assert1.py'])
