#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from utils import similar


def crawler(coName, driver):
    """returns a dictionary with company link and similarity score"""
    url = 'https://www.google.co.in/search?q=' + coName \
        + '+site:https://www.bloomberg.com/research/stocks/private/snapshot.asp'
    driver.get(url)
    driver.save_screenshot('bloom1.png')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'class': 'g'}, limit=2)
    linkScores = {}
    for result in results:
        try:
            resultUrl = result.find('h3', {'class': 'r'}).find('a'
                    )['href']
            # print resultUrl
            driver.get(str(resultUrl))
            # print driver.current_url
            blSoup = BeautifulSoup(driver.page_source, 'html.parser')
            title = blSoup.find('div', {'id': 'columnLeft'}).find('h1'
                    ).find('span').text
            domain = blSoup.find('div',
                                 {'class': 'detailsDataContainerRt'
                                 }).find('a', {'class': 'link_sb'}).text
            score = round(similar(title, coName), 2)
            linkScores[domain] = score
        except AttributeError:
            pass
    return linkScores



			
