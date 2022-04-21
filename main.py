from email.mime import base
from wsgiref import headers
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

baseurl = "https://www.royalcaribbean.com/booking/landing?packageCode=EX06W131&groupId=EX06MIA-638683774&sailDate=2022-05-08&shipCode=EX&destinationCode=CARIB&selectedCurrencyCode=USD"

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))
driver.get(baseurl)
time.sleep(5)
html = driver.page_source
print(html)
