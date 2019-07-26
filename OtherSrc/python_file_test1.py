import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
import ssl
from bs4 import BeautifulSoup

# ssl.create_default_https_context = ssl._create_unverified_context
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
def open_env(url):
    try:
        r = requests.get(url, verify=False)
        print('{}'.format(r.status_code))
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        r.raise_for_status()


def login_td(r, username, password='wuhan02',):

    login_data={
        'login':'pcheng',
        'passwd':'wuhan02',
        'login':'Wait',
        'map':'on'
    }


url = 'https://10.125.2.172/bin-java/login?f=general/login.htm'
username = 'cktest'