import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlencode
from urllib.parse import quote


class personSearch:
    def __init__(self):
        self.chromedriverPath = os.getcwd() + '/dependencies/chromedriver'
        self.person = {}
        self.personQueries = ['firstName','lastName', 'company', 'title', 'school']
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

    def search(self, input_person = None):
        # CLI search
        if not input_person:
            for query in self.personQueries:
                value = input(query + '=')
                if value: 
                    self.person[query] = value
        else: 
            self.person = input_person

        # construct URL and scrape results
        personSearchURL = self.baseURL + urlencode(self.person, quote_via=quote)
        self.browser.get(personSearchURL)
        html = self.browser.page_source
        self.soup = BeautifulSoup(html, 'lxml')

    def getResults(self, n = None, ):
        personResults = self.soup.find_all("span", {"class": "name actor-name"})
        # for each person
        for personResult in personResults: 
            # get their name
            name = personResult.text
            # and the URL to their profile  
            liURL = personResult.parent.parent.parent.attrs['href']
            URL = 'https://www.linkedin.com' + liURL
            self.results += [{'name': name, 'URL': URL}]
        # CLI output
        if not n: 
            n = int(input('# of results?'))
            print(self.results[:n])
        return self.results[:n]

crawler = personSearch()
crawler.connect('AQEDARz6R7AAO180AAABY8dfBtIAAAFj62uK0lYAz8QXn6gzeD8nhfHd3MTNmHrdIni1EV51KoSTXtdcf9yiY1XppYYa-DISIY3cusw_ieSBVPvumyU-yVLe42EQbdFEBfXIRbdRL8sdxl-0jAoie8ua')
crawler.search()
crawler.getResults()









