import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlencode
from urllib.parse import quote


class personSearch:
    def __init__(self):
        self.chromedriverPath = os.getcwd() + '/src/scraper/dependencies/chromedriver'
        self.person = {}
        self.baseURL = 'https://www.linkedin.com/search/results/people/?'
        self.results = []
    
    def connect(self, cookie):
        self.browser = webdriver.Chrome(self.chromedriverPath)
        self.browser.get('https://www.linkedin.com')
        self.cookie = cookie
        self.browser.add_cookie({
            'name': 'li_at',
            'value': self.cookie,
            'domain': '.linkedin.com'
        })

    def search(self, input_person):
        self.person = input_person
        # construct URL and scrape results
        personSearchURL = self.baseURL + urlencode(self.person, quote_via=quote)
        self.browser.get(personSearchURL)
        html = self.browser.page_source
        self.soup = BeautifulSoup(html, 'lxml')

    def getResults(self):
        personResults = self.soup.find_all("span", {"class": "name actor-name"})
        # for each person
        for personResult in personResults: 
            # get their name
            name = personResult.text
            # and the URL to their profile  
            liURL = personResult.parent.parent.parent.attrs['href']
            URL = 'https://www.linkedin.com' + liURL
            self.results += [{'name': name, 'URL': URL}]
        return self.results