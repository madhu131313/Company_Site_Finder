from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from difflib import SequenceMatcher

from crawlers import Google

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
) #AngelList gives 404 error on headless PhantomJS

PHANTOMJS_PATH = "../phantomjs"
coName = raw_input('Enter a Company Name: ')

#driver = webdriver.PhantomJS(PHANTOMJS_PATH)
#driver = webdriver.PhantomJS(PHANTOMJS_PATH, desired_capabilities=dcap)
#driver = webdriver.Firefox()

# Ratcliff/Obershelp Algo for Similarity Score`
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def LinkedinCrawler(coName):
	driver = webdriver.PhantomJS(PHANTOMJS_PATH)
	url = "https://www.google.co.in/search?q="+coName+"+site:www.linkedin.com/company"
	driver.get(url)
	driver.save_screenshot('link1.png')
	soup = BeautifulSoup(driver.page_source,"html.parser")
	result = soup.find_all('div',{'class':'g'},limit=1)
	#print result
	resultUrl = result[0].find('cite').text
	#print resultUrl
	driver.get(str(resultUrl))
	print driver.current_url
	driver.save_screenshot('link.png')
	#print driver.page_source
	lnSoup = BeautifulSoup(driver.page_source,"html.parser")
	#print lnSoup
	domain = lnSoup.find("li",{"class":"website"}).find("a").text.split("//")[-1].split("/")[0]
	print domain
	
	
def AngelCrawler(coName):
	driver = webdriver.PhantomJS(PHANTOMJS_PATH, desired_capabilities=dcap)
	try:
		url= "https://angel.co/search?page=1&q=" + coName +"&type=companies"
		driver.get(url)
		soup = BeautifulSoup(driver.page_source,"html.parser")
		result = soup.find_all('div',{'class':'result'},limit=1)
		driver.save_screenshot('angel0.png')        
		resultUrl = result[0].find("a")['href']
		#print resultUrl
		driver.get(resultUrl)
		#print driver.current_url
		driver.save_screenshot('angel.png')
		agSoup = BeautifulSoup(driver.page_source,"html.parser")
		domain = agSoup.find("a",{"class":"company_url"}).text
		print domain
	except IndexError:
		pass
	
#Google.Crawler(coName)
LinkedinCrawler(coName)
#AngelCrawler(coName)
