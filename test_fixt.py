# test_fixt.py
import pytest


@pytest.fixture()#for scope, 'function' is as default
def login():
    print("请输入账号： ")


def test_s1(login):
    print('test1')


def test_s2():
    print('test2')


def test_s3(login):
    print('test3')


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixt.py'])
