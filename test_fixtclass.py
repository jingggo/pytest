# test_fixtclass.py
import pytest


class TestCase():
    def setup(self):
        print("setup: ")

    def teardown(self):
        print("teardown: ")

    def setup_class(self):
        print("\nsetup_class: ")

    def teardown_class(self):
        print("teardown_class: ")

    def setup_method(self):
        print("setup_method: ")

    def teardown_method(self):
        print("teardown_method: ")

    def test_one(self):
        print("test_one")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("test_two")
        assert 3==3

if __name__ == '__main__':
    pytest.main(['-s', 'test_fixtclass.py'])
