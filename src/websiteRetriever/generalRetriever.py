## General LinkedIn HTML Retriever ##

import os
import time
from bs4 import BeautifulSoup

from selenium import webdriver




class LIGeneralRetriever:

    def __init__(self):
        self.timeout = 10
        self.scroll_increment = 1000 
        self.scroll_pause = .01
        self.scrollEndPause = 3
        self.expandable_button_selectors = []
        return

    # Setup driver and set cookies
    def logIn(self, cookie):
        
        # Set the path of the chromedriver
        chromedriverPath = os.getcwd() + '/dependencies/chromedriver'
            
        # Initiate the webdriver and set the li_at cookie
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        browser = webdriver.Chrome(chromedriverPath, chrome_options=options)
        browser.get('http://www.linkedin.com')
        browser.add_cookie({
            'name': 'li_at',
            'value': cookie,
            'domain': '.linkedin.com'
        })

        # Save the browser to the class instance
        self.browser = browser

    # Place holder for a page loading function 
    def loadPage(self, URL):
        return

    # Private function to scroll and expand entire page
    def _scrollToBottom(self):
        """Scroll to the bottom of the page
        Params:
            - scroll_pause_time {float}: time to wait (s) between page scroll increments
            - scroll_increment {int}: increment size of page scrolls (pixels)
        """
        current_height = 0
        while True:
            for name in self.expandable_button_selectors:
                try:
                    self.browser.find_element_by_css_selector(name).click()
                except:
                    pass
            # Scroll down to bottom
            new_height = self.browser.execute_script(
                "return Math.min({}, document.body.scrollHeight)".format(current_height + self.scroll_increment))
            if (new_height == current_height):
                break
            self.browser.execute_script(
                "window.scrollTo(0, Math.min({}, document.body.scrollHeight));".format(new_height))
            current_height = new_height
            # Wait to load page
            time.sleep(self.scroll_pause)
        time.sleep(self.scrollEndPause)

    def getHTML(self):
        return self.browser.page_source

    # Combination of other funcs to output html given a URL
    def retrieve(self, URL, cookie):
        self.logIn(cookie)
        html = []
        for url in URL:
            self.loadPage(url)
            self._scrollToBottom()
            html.append(self.getHTML())
        # self.browser.quit()
        return html

