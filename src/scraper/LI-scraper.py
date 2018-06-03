## LinkedIn Scraper ##

import requests
import os
from bs4 import BeautifulSoup
from IPython.display import IFrame, HTML
from bs4 import BeautifulSoup
from selenium import webdriver

# Set the path of the chromedriver
chromedriverPath = os.getcwd() + '/src/scraper/dependencies/chromedriver'

# Initiate the webdriver and set the li_at cookie
browser = webdriver.Chrome(chromedriverPath)
browser.get('http://www.linkedin.com')
cookie = 'AQEDARz6R7AAO180AAABY8dfBtIAAAFj62uK0lYAz8QXn6gzeD8nhfHd3MTNmHrdIni1EV51KoSTXtdcf9yiY1XppYYa-DISIY3cusw_ieSBVPvumyU-yVLe42EQbdFEBfXIRbdRL8sdxl-0jAoie8ua'
browser.add_cookie({
    'name': 'li_at',
    'value': cookie,
    'domain': '.linkedin.com'
})

# Retrieve html in xml format from a url
url = 'https://www.linkedin.com/in/nick-bunn-793244114/'
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

print(soup)
