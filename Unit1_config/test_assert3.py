# test_assert3.py
import pytest


def test_zero_division():
    """断言异常"""
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

    # 断言异常类型type
    assert excinfo.type == ZeroDivisionError
    # 断言异常value
    assert "division by zero" in str(excinfo.value)


if __name__ == '__main__':
    pytest.main(['-s', 'test_assert3.py'])
