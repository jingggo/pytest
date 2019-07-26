# test_define_mark1.py
import pytest


@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest for you app

def test_sth_quick():
    pass

def test_another():
    pass

class TestClass:
    def test_method(self):
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'test_define_mark1.py', '-m=webtest'])
