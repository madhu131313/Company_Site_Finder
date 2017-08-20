from selenium import webdriver
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import tldextract;

import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

# Ratcliff/Obershelp Algo for Similarity Score`
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def crawler(coName):
	driver = webdriver.PhantomJS(data['PHANTOMJS_PATH'])
	url = "https://www.google.co.in/search?q="+ coName 
	driver.get(url)
	driver.save_screenshot('link.png')
	soup = BeautifulSoup(driver.page_source,"html.parser")
	results = soup.find_all('div',{'class':'g'}, limit=3)
	linkScores = {}
	for result in results:
                #driver.save_screenshot('google.png')
                #print result
                try:
                        title =  result.find('h3', {'class':'r'}).find('a').text
                        score = round(similar(title, coName),2)
                        #print title
                        domain = result.find('cite').text.split("//")[-1].split("/")[0]
                except AttributeError:
                        pass
                #Filtering out results from News 
                if " " in domain or "." not in domain:
                        continue
                #extracts domain from a sitename. ex: bbc from forums.bbc.co.uk
                mainDomain = tldextract.extract(domain).domain
                #Filtering out Fb, linkedin, wikipedia, glassdoor, google
                print mainDomain
                if mainDomain not in coName and mainDomain in data['Google_exlude']:
                        continue                
                if mainDomain in coName or coName in mainDomain or similar(mainDomain, coName) > 0.6:
                        score = 1
                         
		linkScores[domain] = score
		print domain + " " + str(score)
        
