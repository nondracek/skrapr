## Company HTML Retriever ##

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import os
import sys
packagePath = os.getcwd().replace('/src/websiteRetriever','')
sys.path.append(packagePath)

from utils import AnyEC

from generalRetriever import LIGeneralRetriever

class LICompanyRetriever(LIGeneralRetriever):
    
    def __init__(self, browser):
        super().__init__(browser)

        self.expandable_button_selectors = [
            'button[aria-expanded="false"].org-about-company-module__show-details-button'
        ]


    # Retrieve full page  HTML from URL
    def loadPage(self, URL):
        self.browser.get(URL)
        try:
            attemptLoad = WebDriverWait(self.browser, self.timeout).until(
                    AnyEC(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '.org-top-card-module')),
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '.error-illustration'))
            ))
        except TimeoutException as err:
            raise ValueError(
                """Took too long to load company.  Common problems/solutions:
                1. Invalid LI_AT value: ensure that yours is correct (they
                   update frequently)
                2. Slow Internet: increase the timeout parameter in the Scraper""")
        # Check if we reached a valid profile
        try:
            self.browser.find_element_by_css_selector('.org-top-card-module')
        except:
            raise ValueError(
                'Company Unavailable: Company link does not match any current Linkedin Companies')

