# test_assert2.py
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_assert2.py'])
