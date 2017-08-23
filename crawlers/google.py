#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import tldextract
from utils import similar, get_config


def crawler(coName, driver):
    """returns a dictionary with company link and similarity score"""
    google_exclude = get_config()['Google_exclude']
    url = 'https://www.google.co.in/search?q=' + coName
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'class': 'g'}, limit=3)
    linkScores = {}
    for result in results:
        try:
            title = result.find('h3', {'class': 'r'}).find('a').text
            score = round(similar(title, coName), 2)
            domain = result.find('cite').text.split('//')[-1].split('/'
                    )[0]
        except AttributeError:
            continue
        # Filtering out results from News
        if ' ' in domain or '.' not in domain:
            continue
        # extracts domain from a sitename. ex: bbc from forums.bbc.co.uk
        mainDomain = tldextract.extract(domain).domain
        # Filtering out Fb, linkedin, wikipedia, glassdoor, google
        if mainDomain not in coName and mainDomain in google_exclude:
            continue
        if mainDomain in coName or coName.replace(' ', '').lower() \
            in mainDomain or similar(mainDomain, coName) > 0.5:
            score = 1
        linkScores[domain] = score
    return linkScores
