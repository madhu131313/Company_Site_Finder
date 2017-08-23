#!/usr/bin/python
# -*- coding: utf-8 -*-
from crawlers import google, angel, linkedin, bloomberg
from driver import driver


def hi_link(domains):
    """returns link with highest similarity score"""
    if len(domains) == 0:
        return None
    highest =  max(domains.iterkeys(), key=lambda key: domains[key]) #link with highest score
    if domains[highest] >= 0.5:
        return highest
    else:
        return None


def domain_filter(bl_domains, al_domains, gg_domains):
    """Returns a final predicte domain"""

    if hi_link(bl_domains):
        return hi_link(bl_domains)

    if hi_link(al_domains):
        return hi_link(al_domains)

    if hi_link(gg_domains):
        return hi_link(gg_domains)

    return None


if __name__ == '__main__':
    co_name = raw_input('Enter a Company Name: ')
    webdriver = driver()

    bl_domains = bloomberg.crawler(co_name, webdriver)
    gg_domains = google.crawler(co_name, webdriver)
    #ln_domains = linkedin.crawler(co_name) #Login Redirection issue
    al_domains = angel.crawler(co_name, webdriver)

    domain = domain_filter(bl_domains, al_domains, gg_domains)

    if domain:
        print 'Company website is ' + domain
    else:
        print "Couldn't find the company website"

    webdriver.quit()


			
