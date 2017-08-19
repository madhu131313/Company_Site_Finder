from difflib import SequenceMatcher
from crawlers import Google, Angel, Linkedin

PHANTOMJS_PATH = "../phantomjs"
coName = raw_input('Enter a Company Name: ')


# Ratcliff/Obershelp Algo for Similarity Score`
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

	
#Google.Crawler(coName)
Linkedin.Crawler(coName)
#Angel.Crawler(coName)
