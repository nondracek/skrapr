import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlencode
from urllib.parse import quote

# empty dictionary of person query info
person = {}
# list of query parameters
personQueries = ['firstName','lastName', 'company', 'title', 'school']
# get parameters from user
for query in personQueries:
    value = input(query + '=')
    if value: 
        person[query] = value
baseURL = 'https://www.linkedin.com/search/results/people/?'
# append query to URL in correct encoding
personSearchURL = baseURL + urlencode(person, quote_via=quote)

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
browser.get(personSearchURL)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

# empty list for search result URLs
results = []
# find people in results
personResults = soup.find_all("span", {"class": "name actor-name"})
# for each person
for personResult in personResults: 
    # get their name
    name = personResult.text
    # and the URL to their profile  
    liURL = personResult.parent.parent.parent.attrs['href']
    URL = 'https://www.linkedin.com' + liURL
    results += [{'name': name, 'URL': URL}]

n = int(input('# of results?'))

print(results[:n])

