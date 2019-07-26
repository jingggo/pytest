# test_skip2.py
import pytest
import mymodule

minversion = pytest.mark.skipif(mymodule.__versioninfo__ < (1,1),
                                reason="at least mymodule-1.1 required")
@minversion
def test_anotherfunction():
    assert True


if __name__ == '__main__':
    pytest.main(['-q', 'test_skip2.py'])
