from selenium import webdriver
from bs4 import BeautifulSoup
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

def Crawler(coName):
	driver = webdriver.PhantomJS(data['PHANTOMJS_PATH'])
	url = "https://www.google.co.in/search?q="+ coName 
	driver.get(url)
	driver.save_screenshot('link.png')
	soup = BeautifulSoup(driver.page_source,"html.parser")
	results = soup.find_all('div',{'class':'g'}, limit=3)
	for result in results:
                #print result
		title =  result.find('h3', {'class':'r'}).find('a').text
		print title
		domain = result.find('cite').text.split("//")[-1].split("/")[0]
		print domain
