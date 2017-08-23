from crawlers import google, angel, linkedin, bloomberg
from driver import driver

def domain_filter(bl_domains, al_domains, gg_domains): 
    for bl_domain in bl_domains: #Bloomberg
        if bl_domains[bl_domain] > 0.5:
            return bl_domain
    for al_domain in al_domains: #AngelList
        if al_domains[al_domain] > 0.6:
             return al_domain             
    for gg_domain in gg_domains: #Google
        if gg_domains[gg_domain] > 0.5:
            return gg_domain
    return None
    

if __name__ == "__main__":
    
    co_name = raw_input('Enter a Company Name: ')
    webdriver = driver()
    
    bl_domains = bloomberg.crawler(co_name, webdriver)	
    gg_domains = google.crawler(co_name, webdriver)
    #ln_domains = linkedin.crawler(co_name) #Login Redirection issue
    al_domains = angel.crawler(co_name, webdriver)

    domain = domain_filter(bl_domains, al_domains, gg_domains)

    if domain:
        print "Company website is " + domain
    else:
        print "Couldn't find the company website"

    webdriver.quit()
                
