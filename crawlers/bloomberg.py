from selenium import webdriver
from bs4 import BeautifulSoup
import json
from difflib import SequenceMatcher
import signal

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

# Ratcliff/Obershelp Algo for Similarity Score`
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def crawler(coName):
	driver = webdriver.PhantomJS(data['PHANTOMJS_PATH'])
	url = "https://www.google.co.in/search?q="+coName+"+site:https://www.bloomberg.com/research/stocks/private/snapshot.asp"
	driver.get(url)
	#driver.save_screenshot('bloom1.png')
	soup = BeautifulSoup(driver.page_source,"html.parser")
	results = soup.find_all('div',{'class':'g'},limit=2)
	linkScores = {}
	for result in results:
                try:
                    resultUrl = "http://google.com" + result.find("h3", {'class':'r'}).find('a')['href']
                    #print resultUrl
                    driver.get(str(resultUrl))
                    #print driver.current_url
                    #driver.save_screenshot('link.png')
                    #print driver.page_source
                    blSoup = BeautifulSoup(driver.page_source,"html.parser")
                    title = blSoup.find("div", {"id":"columnLeft"}).find('h1').find('span').text
                    domain = blSoup.find("div", {"class":"detailsDataContainerRt"}).find("a", {"class":"link_sb"}).text
                    score = round(similar(title, coName),2)
                    linkScores[domain] = score
                except AttributeError:
                        pass
        driver.service.process.send_signal(signal.SIGTERM)
        driver.quit()        
	return linkScores
	
	
