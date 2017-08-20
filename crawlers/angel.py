from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from difflib import SequenceMatcher
import signal

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

# Ratcliff/Obershelp Algo for Similarity Score`
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

#AngelList gives 404 error on headless PhantomJS
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
	"(KHTML, like Gecko) Chrome/15.0.87"
) 

def crawler(coName):
	driver = webdriver.PhantomJS(data['PHANTOMJS_PATH'], desired_capabilities=dcap)
	linkScores = {}
	try:
		url= "https://angel.co/search?page=1&q=" + coName +"&type=companies"
		driver.get(url)
		soup = BeautifulSoup(driver.page_source,"html.parser")
		result = soup.find_all('div',{'class':'result'},limit=1)
		driver.save_screenshot('angel0.png')        
		resultUrl = result[0].find("a")['href']
		title = result[0].find('div', {'class':'title'}).find("a").text 
		#print resultUrl
		driver.get(resultUrl)
		#print driver.current_url
		driver.save_screenshot('angel.png')
		agSoup = BeautifulSoup(driver.page_source,"html.parser")
		domain = agSoup.find("a",{"class":"company_url"}).text
		score = round(similar(title, coName),2)
		linkScores[domain] = score
		#print domain
		#print title
		#print score
	except (IndexError, AttributeError) as e:
		pass
	driver.service.process.send_signal(signal.SIGTERM)
        driver.quit()
        return linkScores
