# test_teardown_f3.py
import pytest
import smtplib


@pytest.fixture(scope='module')
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()
    request.addfinalizer(fin)
    return smtp_connection  # provide the fixture value


