# test_teardown_f1.py
import pytest

# 如果其中一个用例出现异常，不影响yield后面的teardown执行，运行结果互不影响，并且全部用例执行完之后，yield呼唤teardown操作
# 如果在setup就异常了，那么是不会去执行yield后面的teardown
# yield也可以配合with语句，以下是官方文档给的案例
@pytest.fixture(scope='module')
def open():
    print("打开浏览器，并且打开百度首页")

    yield
    print("执行teardown!")
    print("最后关闭浏览器")


def test_s1(open):
    print("test case1")
    raise NameError


def test_s2(open):
    print("test case2")


def test_s3(open):
    print("test case3")


if __name__ == '__main__':
    pytest.main(['-q', 'test_teardown_f1.py'])
