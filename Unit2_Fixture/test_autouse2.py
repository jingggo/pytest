# test_autouse2.py
import pytest
import time

@pytest.fixture(scope='module', autouse=True)
def start(request):
    print('\n-----开始执行module-----')
    print('module   : %s' % request.module.__name__)
    print('------启动浏览器------')
    yield
    print('------结束测试------')


class Test_aaa():
    @pytest.fixture(scope='function', autouse=True)
    def open_home(self, request):
        print('function: %s \n ------回到首页------' % request.function.__name__)

    def test_01(self):
        print('------用例1------')

    def test_02(self):
        print('-----用例2-----')


if __name__ == '__main__':
    pytest.main(['-s', 'test_autouse2.py'])
