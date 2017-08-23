#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def crawler(coName, driver):
    """returns a dictionary with company link and similarity score"""
    url = 'https://www.google.co.in/search?q=' + coName \
        + '+site:www.linkedin.com/company'
    driver.get(url)
    driver.save_screenshot('link1.png')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    result = soup.find_all('div', {'class': 'g'}, limit=1)
    #print result
    linkScores = {}
    try:
        if len(result) > 0:
            resultUrl = result[0].find('cite').text
            driver.get(str(resultUrl))
            print driver.current_url
            driver.save_screenshot('link.png')
            print driver.page_source
            lnSoup = BeautifulSoup(driver.page_source, 'html.parser')
            title = lnSoup.find('h1', {'class': 'name'}).text
            print title
            domain = lnSoup.find('li', {'class': 'website'})
            domain = domain.find('a').text.split('//')[-1].split('/')[0]
            score = round(similar(title, coName), 2)
            linkScores[domain] = score
    except AttributeError:
        pass
    return linkScores



			
