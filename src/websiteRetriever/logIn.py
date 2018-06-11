import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class logIn():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.getCookie()

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
        
        self.cookie = client.cookies['li_at']

    # Setup driver and set cookies
    def logIn(self):

        # Set the path of the chromedriver
        chromedriverPath = '../dependencies/chromedriver'
            
        # Initiate the webdriver and set the li_at cookie
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        browser = webdriver.Chrome(chromedriverPath, chrome_options=options)
        browser.get('http://www.linkedin.com')
        browser.add_cookie({
            'name': 'li_at',
            'value': self.cookie,
            'domain': '.linkedin.com'
        })

        # Return the browser
        return browser


