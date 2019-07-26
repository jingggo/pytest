import pytest


class TestCase():
    def test_something1(self):
        x= 'this'
        assert 'h' in x

    def test_something2(self):
        x= 'hello'
        assert hasattr(x, 'check')

if __name__ == '__main__':
    pytest.main(['-q', 'test_class.py'])
