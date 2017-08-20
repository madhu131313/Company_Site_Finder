from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
	"(KHTML, like Gecko) Chrome/15.0.87"
) #AngelList gives 404 error on headless PhantomJS

def crawler(coName):
	driver = webdriver.PhantomJS(data['PHANTOMJS_PATH'], desired_capabilities=dcap)
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
