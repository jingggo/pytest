# test_teardown_f2.py
import pytest
import smtplib

@pytest.fixture(scope='module')
def smtp():
    with smtplib.SMTP('smtp.gmail.com') as smtp:
        yield smtp


if __name__ == '__main__':
    pytest.main(['-s', 'test_teardown_f2.py'])
