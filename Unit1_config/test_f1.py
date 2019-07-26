# test_f1.py
import pytest

#
@pytest.fixture(scope='module')
def open():
    print("打开浏览器，并且打开百度首页")


def test_s1(open):
    print("test case1")


def test_s2(open):
    print("test case2")


def test_s3(open):
    print("test case3")


if __name__ == '__main__':
    pytest.main(['-s', 'test_f1.py'])
