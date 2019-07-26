# test_param1.py
import pytest

# pytest.param("6*9",42,marks=pytest.mark.xfail) 标记单个测试实例在参数化
@pytest.mark.parametrize("test_input,expected",
                         [
                             ("3+5", 8),
                             ("2+4", 6),
                             pytest.param("6*9",42,marks=pytest.mark.xfail),
                         ])
def test_eval(test_input, expected):
    print("--------------Start Test-------------------")
    assert eval(test_input)==expected


if __name__ == '__main__':
    pytest.main(['-s', 'test_param1.py'])
