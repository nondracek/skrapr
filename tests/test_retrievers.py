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
from logIn import logIn

def test_profile_retriever():
    URL = ['https://www.linkedin.com/in/nick-bunn-793244114/']
    LI = logIn('robertriever@gmail.com', 'RoboRetriever123')
    browser = LI.logIn()
    LIPR =  LIProfileRetriever(browser)
    LIPR.retrieve(URL)

def test_company_retriever():
    Company_URL = ['https://www.linkedin.com/company/harvard-student-agencies/']
    LI = logIn('robertriever@gmail.com', 'RoboRetriever123')
    browser = LI.logIn()
    LICR = LICompanyRetriever(browser)
    LICR.retrieve(Company_URL)
