from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

with open('./config.json') as json_data_file:
    data = json.load(json_data_file)

#AngelList gives 404 error on default PhantomJS user agent
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
	"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"
) 

def driver():
    return webdriver.PhantomJS(data['PHANTOMJS_PATH'], desired_capabilities=dcap)
