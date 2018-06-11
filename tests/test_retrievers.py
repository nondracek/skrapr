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
from cookieRetriever import cookieRetriever

def test_profile_retriever():
    URL = ['https://www.linkedin.com/in/nick-bunn-793244114/']
    CR = cookieRetriever('username', 'password')
    cookie = CR.getCookie()
    LIPR =  LIProfileRetriever()
    LIPR.retrieve(URL, cookie)
    assert True

def test_company_retriever():
    Company_URL = ['https://www.linkedin.com/company/harvard-student-agencies/']
    CR = cookieRetriever('username', 'password')
    cookie = CR.getCookie()
    LICR = LICompanyRetriever()
    LICR.retrieve(Company_URL, cookie)
    assert True
