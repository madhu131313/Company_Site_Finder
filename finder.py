from selenium import webdriver
from bs4 import BeautifulSoup

PHANTOMJS_PATH = "../phantomjs"

coName="razorpay"
driver = webdriver.PhantomJS(PHANTOMJS_PATH) 


def GoogleCrawler(driver, coName):
	url = "https://www.google.co.in/search?q="+ coName +"+-linkedin+-facebook+-twitter+-wikipedia+-glassdoor+-zaubacorp+-bloomberg"
	driver.get(url)
	soup = BeautifulSoup(driver.page_source,"html.parser")
	results = soup.find_all('div',{'class':'g'}, limit=3)
	for result in results:
		domain = result.find('cite').text.split("//")[1].split("/")[0]
		print domain

def LinkedinCrawler(driver, coName):
        url = "https://www.google.co.in/search?q="+coName+"+site:www.linkedin.com/company"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,"html.parser")
        result = soup.find_all('div',{'class':'g'},limit=1)
        print result
        resultUrl = result[0].find('cite').text
        print resultUrl
        driver.get(str(resultUrl))
        #print driver.page_source
        lnSoup = BeautifulSoup(driver.page_source,"html.parser")
        #print lnSoup
        domain = lnSoup.find("li",{"class":"website"}).find("a").text.split("//")[1].split("/")[0]
        print domain
        
def AngelCrawler(driver, coName):
        url= "https://angel.co/search?page=1&q=" + coName +"&type=companies"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,"html.parser")
        result = soup.find_all('div',{'class':'result'},limit=1)
        #print result
        resultUrl = result[0].find("a")['href']
        print resultUrl
        driver.get(str(resultUrl))
        agSoup = BeautifulSoup(driver.page_source,"html.parser")
        print agSoup
        domain = agSoup.find("a",{"class":"company_url"}).text.split("//")[1].split("/")[0]
        print domain
        
#GoogleCrawler(driver, coName)
#LinkedinCrawler(driver,coName)
AngelCrawler(driver, coName)

