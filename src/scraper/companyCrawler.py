import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlencode
from urllib.parse import quote


class companySearch:
    def __init__(self):
        self.chromedriverPath = os.getcwd() + '/dependencies/chromedriver'
        self.company = {}
        self.baseURL ='https://www.linkedin.com/search/results/companies/?'
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

    def search(self, input_company = None):
        # CLI search
        if not input_company:
            self.company['keywords'] = input("Search?")
        else: 
            self.company= input_company
        # construct URL and scrape results
        companySearchURL = self.baseURL + urlencode(self.company, quote_via=quote)
        self.browser.get(companySearchURL)
        html = self.browser.page_source
        self.soup = BeautifulSoup(html, 'lxml')

    def get_results(self, n = None, ):
        companyResults = self.soup.find_all("div", {"class": "search-result__info"})
        # for each company
        for companyResult in companyResults: 
            # get their name
            name = companyResult.find('a', {"class": "search-result__result-link"}).text.lstrip().rstrip()
            # and the URL to their profile  
            liURL = companyResult.find('a', {"class": "search-result__result-link"}).attrs['href']
            URL = 'https://www.linkedin.com' + liURL
            # Get their industry
            industry = companyResult.find('p', {'class': "subline-level-1"}).text.lstrip().rstrip()
            self.results += [{'name': name, 'URL': URL, 'industry': industry}]
        # CLI output
        if not n: 
            n = int(input('# of results?'))
            print(self.results[:n])
        return self.results[:n]

crawler =companySearch()
crawler.connect('AQEDARz6R7AAO180AAABY8dfBtIAAAFj62uK0lYAz8QXn6gzeD8nhfHd3MTNmHrdIni1EV51KoSTXtdcf9yiY1XppYYa-DISIY3cusw_ieSBVPvumyU-yVLe42EQbdFEBfXIRbdRL8sdxl-0jAoie8ua')
crawler.search()
crawler.get_results()










