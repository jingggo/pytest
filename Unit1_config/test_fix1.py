# test_fix1.py
import pytest


def test_s1(login):
    print('test1')


def test_s2():
    print('test2')


def test_s3(login):
    print('test3')


if __name__ == '__main__':
    pytest.main(['-s', 'test_fix1.py'])