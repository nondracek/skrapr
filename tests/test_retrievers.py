import pytest
import os
import sys
packagePath = os.getcwd().replace('/tests','') 
retrieverPath = packagePath + '/src/websiteRetriever'
sys.path.append(packagePath)
sys.path.append(retrieverPath)
print(sys.path)
from profileRetriever import LIProfileRetriever
from companyRetriever import LICompanyRetriever

cookie = 'AQEDARz6R7AAO180AAABY8dfBtIAAAFj62uK0lYAz8QXn6gzeD8nhfHd3MTNmHrdIni1EV51KoSTXtdcf9yiY1XppYYa-DISIY3cusw_ieSBVPvumyU-yVLe42EQbdFEBfXIRbdRL8sdxl-0jAoie8ua'

def test_profile_retriever():
    URL = ['https://www.linkedin.com/in/nick-bunn-793244114/']
    LIPR =  LIProfileRetriever()
    LIPR.retrieve(URL, cookie)
    assert True

def test_company_retriever():
    Company_URL = ['https://www.linkedin.com/company/harvard-student-agencies/']
    LICR = LICompanyRetriever()
    LICR.retrieve(Company_URL, cookie)
    assert True
