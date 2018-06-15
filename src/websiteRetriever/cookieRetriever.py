import requests
from bs4 import BeautifulSoup


class cookieRetriever():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getCookie(self):
        client = requests.Session()
        
        HOMEPAGE_URL = 'https://www.linkedin.com'
        LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
        
        html = client.get(HOMEPAGE_URL).content
        soup = BeautifulSoup(html, "html.parser")
        csrf = soup.find(id="loginCsrfParam-login")['value']
        
        login_information = {
            'session_key': self.username,
            'session_password': self.password,
            'loginCsrfParam': csrf,
        }
        
        client.post(LOGIN_URL, data=login_information)
        
        return client.cookies['li_at']
