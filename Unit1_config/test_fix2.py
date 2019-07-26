# test_fix2.py
import pytest


def test_s4(login):
    print('test4')


def test_s5():
    print('test5')


if __name__ == '__main__':
    pytest.main(['-s', 'test_fix2.py'])
