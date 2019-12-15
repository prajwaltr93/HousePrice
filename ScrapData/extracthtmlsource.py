from selenium.webdriver import Firefox
from time import sleep
from bs4 import BeautifulSoup as bs
import html.parser
browser = Firefox()

base_url = "https://www.99acres.com/rent-property-in-bangalore-ffid-page-"
limit = int(input("enter the browsing limit : "))
for i in range(1,limit+1):
    browser.get(base_url+str(i))
    sleep(2)
    with open("./htmlfiles/page-"+str(i)+".txt","w") as file:
        file.write(bs(browser.page_source,"html.parser").prettify())
browser.close()
