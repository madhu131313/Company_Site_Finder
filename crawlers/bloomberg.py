from selenium import webdriver
from bs4 import BeautifulSoup
import json
from difflib import SequenceMatcher

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

# Ratcliff/Obershelp Algo for Similarity Score`
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def crawler(coName):
	driver = webdriver.PhantomJS(data['PHANTOMJS_PATH'])
	url = "https://www.google.co.in/search?q="+coName+"+site:https://www.bloomberg.com/research/stocks/private/snapshot.asp"
	driver.get(url)
	driver.save_screenshot('bloom1.png')
	soup = BeautifulSoup(driver.page_source,"html.parser")
	results = soup.find_all('div',{'class':'g'},limit=2)
	linkScores = {}
        for result in results:
            resultUrl = result.find('cite').text
            #print resultUrl
	    driver.get(str(resultUrl))
	    print driver.current_url
	    driver.save_screenshot('link.png')
	    #print driver.page_source
	    blSoup = BeautifulSoup(driver.page_source,"html.parser")
	    domain = blSoup.find("a", {"class":"link_sb"})['href']
	    print domain
           
"""            
	if len(results) > 0:
                        resultUrl = result[0].find('cite').text
			#print resultUrl
			driver.get(str(resultUrl))
			print driver.current_url
			driver.save_screenshot('link.png')
			print driver.page_source
			lnSoup = BeautifulSoup(driver.page_source,"html.parser")
			#print lnSoup
			title = lnSoup.find("h1", {"class":"name"}).text
			print title
			domain = lnSoup.find("li",{"class":"website"})
			#print domain
			domain= domain.find("a").text.split("//")[-1].split("/")[0]
			score = round(similar(title, coName),2)
			linkScores[domain] = score
			print domain
        return linkScores
"""
