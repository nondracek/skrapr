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

class LIProfileRetriever(LIGeneralRetriever):
    def __init__(self, browser):
        super().__init__(browser)


        self.expandable_button_selectors = [
            'button[aria-expanded="false"].pv-skills-section__additional-skills',
            'button[aria-expanded="false"].pv-profile-section__see-more-inline',
            'button[aria-expanded="false"].pv-top-card-section__summary-toggle-button',
            'button[data-control-name="contact_see_more"]'
        ]
        return


    # Retrieve full page  HTML from URL
    def loadPage(self, URL):
        self.browser.get(URL)
        try:
            attemptLoad = WebDriverWait(self.browser, self.timeout).until(
                    AnyEC(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '.pv-top-card-section')),
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '.profile-unavailable'))
            ))
        except TimeoutException as err:
            raise ValueError(
                """Took too long to load profile.  Common problems/solutions:
                1. Invalid LI_AT value: ensure that yours is correct (they
                   update frequently)
                2. Slow Internet: increase the timeout parameter in the Scraper constructor""")
        # Check if we reached a valid profile
        try:
            self.browser.find_element_by_css_selector('.pv-top-card-section')
        except:
            raise ValueError(
                'Profile Unavailable: Profile link does not match any current Linkedin Profiles')
