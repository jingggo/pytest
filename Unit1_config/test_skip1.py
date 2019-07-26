# test_skip1.py
import pytest
import sys

# 标记测试用例在Python3.7之前的解释器上运行时要跳过的函数
@pytest.mark.skipif(sys.version_info < (3, 7),
                    reason="requires python3.7 or higher")
def test_f():
    assert True


if __name__ == '__main__':
    pytest.main(['-q', 'test_skip1.py'])
