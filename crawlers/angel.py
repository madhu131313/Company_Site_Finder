#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from utils import similar


def crawler(coName, driver):
    """returns a dictionary with company link and similarity score"""
    linkScores = {}
    try:
        url = 'https://angel.co/search?page=1&q=' + coName \
            + '&type=companies'
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        result = soup.find_all('div', {'class': 'result'}, limit=1)
        # driver.save_screenshot('angel0.png')
        resultUrl = result[0].find('a')['href']
        title = result[0].find('div', {'class': 'title'}).find('a').text
        # print resultUrl
        driver.get(resultUrl)
        # print driver.current_url
        # driver.save_screenshot('angel.png')
        agSoup = BeautifulSoup(driver.page_source, 'html.parser')
        domain = agSoup.find('a', {'class': 'company_url'}).text
        score = round(similar(title, coName), 2)
        linkScores[domain] = score
    except (IndexError, AttributeError), e:
        pass
    return linkScores



			
