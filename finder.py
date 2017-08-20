from crawlers import google, angel, linkedin, bloomberg

coName = raw_input('Enter a Company Name: ')


blDomains = bloomberg.crawler(coName)	
ggDomains = google.crawler(coName)
#lnDomains = linkedin.crawler(coName) #Login Redirection issue
alDomains = angel.crawler(coName)


def domain_filter(blDomains, alDomains, ggDomains): 
    for blDomain in blDomains: #Bloomberg
        if blDomains[blDomain] > 0.5:
            print "Company Site is " + blDomain
            return
    for alDomain in alDomains: #AngelList
        if alDomains[alDomain] > 0.6:
             print "Company Site is " + alDomain
             return
    for ggDomain in ggDomains: #Google
        if ggDomains[ggDomain] > 0.5:
            print "Company Site is " + ggDomain
            return
    print "Couldn't find the company website"
    
domain_filter(blDomains, alDomains, ggDomains)  
                
