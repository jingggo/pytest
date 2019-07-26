"""
test_.*.py/.*_test.py in this package can use methods in this file
单独运行test_fix1 and test_fix2 都能调用 login

fixture(scope='function', params=None, autouse=False, ids=None, Name=None)
scope: function, module, class, session

@Author:jyang
@Date:7/23/2019
"""
import pytest


@pytest.fixture()
def login():
    print("Please input user name and password.")
