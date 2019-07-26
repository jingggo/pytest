# test_fixt.py
import pytest


def setup_module():
    print("\nsetup_module: 整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")


def teardown_module():
    print("teardown_module:  整个.py模块只执行一次")
    print("比如：所有用例结束后只关闭浏览器")

def setup_function():
    print("每个用例执行前都会执行")


def teardown_function():
    print("每个用例结束后都会执行")


def test_one():
    print("--- 正在执行test_one")
    x = 'this'
    assert 'h' in x

def test_two():
    print("--- 正在执行test_two")
    x = 'hello'
    assert hasattr(x, 'h')


def test_three():
    print("--- 正在执行test_three")
    a = 'hello'
    b = 'hello world'
    assert a in b


if __name__ == '__main__':
    pytest.main(['-s', 'test_pre.py'])
