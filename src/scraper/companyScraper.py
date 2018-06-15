from bs4 import BeautifulSoup


class companyScraper():
    # takes a broswer fully loaded on the correct page
    def __init__(self, browser):
        html = browser.page_source
        self.soup = BeautifulSoup(html, 'lxml')
    
    # pareses information and returns it as dictionary
    def scrape(self):
        industry = self.soup.find(
            'span', {'class': 'company-industries'}).text.lstrip().rstrip()
        location = self.soup.find(
            'span', {
                'class': 'org-top-card-module__location'}).text.lstrip().rstrip()
        description = self.soup.find(
            'p', {
                'class': 'org-about-us-organization-description__text'}).text.lstrip().rstrip()
        peopleAtCompamyLink = self.soup.find(
            'a', {
                'class': 'org-company-employees-snackbar__details-highlight snackbar-description-see-all-link link-without-visited-state ember-view'}).attrs['href']
        url = self.soup.find(
            'a', {
                'class': 'org-about-us-company-module__website'}).attrs['href']
        headquarters = self.soup.find(
            'p', {'class': 'org-about-company-module__headquarters'}).text.rstrip().lstrip()
        foundYear = int(
            self.soup.find(
                'p', {
                    'class': 'org-about-company-module__founded'}).text.rstrip().lstrip())
        companyType = self.soup.find(
            'p', {'class': 'org-about-company-module__company-type'}).text.rstrip().lstrip()
        sizeRange = self.soup.find(
            'p', {
                'class': 'org-about-company-module__company-staff-count-range'}).text.rstrip().lstrip()
        specialties = self.soup.find(
            'p', {'class': 'org-about-company-module__specialities'}).text.rstrip().lstrip()
        data = {
            'industry': industry,
            'location': location,
            'description': description,
            'peopleAtCompamyLink': peopleAtCompamyLink,
            'url': url,
            'headquarters': headquarters,
            'foundYear': foundYear,
            'companyType': companyType,
            'sizeRange': sizeRange,
            'specialties': specialties}
        return data
