import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlencode
from urllib.parse import quote


company = {}
company['keywords'] = input("Search?")
baseURL = 'https://www.linkedin.com/search/results/companies/?'
# append query to URL in correct encoding
companySearchURL = baseURL + urlencode(company, quote_via=quote)

# all old code for navigation
###########################
# Set the path of the chromedriver
chromedriverPath = os.getcwd() + '/dependencies/chromedriver'

# Initiate the webdriver and set the li_at cookie
browser = webdriver.Chrome(chromedriverPath)
browser.get('https://www.linkedin.com')
cookie = 'AQEDARz6R7AAO180AAABY8dfBtIAAAFj62uK0lYAz8QXn6gzeD8nhfHd3MTNmHrdIni1EV51KoSTXtdcf9yiY1XppYYa-DISIY3cusw_ieSBVPvumyU-yVLe42EQbdFEBfXIRbdRL8sdxl-0jAoie8ua'
browser.add_cookie({
    'name': 'li_at',
    'value': cookie,
    'domain': '.linkedin.com'
})
###########################

# go to search URL
# Retrieve html in xml format from a url
browser.get(companySearchURL)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

# empty list for search result URLs
results = []
# find people in results
companyResults = soup.find_all("div", {"class": "search-result__info"})
# for each person
for companyResult in companyResults: 
    # get their name
    name = companyResult.find('a', {"class": "search-result__result-link"}).text.lstrip().rstrip()
    # and the URL to their profile  
    liURL = companyResult.find('a', {"class": "search-result__result-link"}).attrs['href']
    URL = 'https://www.linkedin.com' + liURL
    # Get their industry
    industry = companyResult.find('p', {'class': "subline-level-1"}).text.lstrip().rstrip()
    results += [{'name': name, 'URL': URL, 'industry': industry}]

n = int(input('# of results?'))

print(results[:n])

