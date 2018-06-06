import personCrawler 
import companyCrawler

class cli:

    def __init__(self):
        self.personQueries = ['firstName','lastName', 'company', 'title', 'school']

    def __searchType(self):
        self.isPerson = int(input('Looking for a company(0) or person(1) ? '))
        return self.isPerson
    
    def __searchQuery(self):
        if self.isPerson:
            self.person = {}
            for query in self.personQueries:
                value = input(query + '= ')
                if value: 
                    self.person[query] = value
            return self.person
        else:
            self.company = {}
            self.company['keywords'] = input("Search? ")
            return self.company
    
    def __resultNumber(self): 
        maxResult = len(self.results)
        return min(int(input('# of results out of %i? ' %maxResult)), maxResult)


    def runSearch(self): 
        if self.__searchType():
            self.crawler = personCrawler.personSearch()
        else: 
            self.crawler = companyCrawler. companySearch()
        self.crawler.connect('AQEDARz6R7AAO180AAABY8dfBtIAAAFj62uK0lYAz8QXn6gzeD8nhfHd3MTNmHrdIni1EV51KoSTXtdcf9yiY1XppYYa-DISIY3cusw_ieSBVPvumyU-yVLe42EQbdFEBfXIRbdRL8sdxl-0jAoie8ua')
        self.crawler.search(self.__searchQuery())
        self.results = self.crawler.getResults()
        print(self.results[:self.__resultNumber()])

search = cli()
search.runSearch()