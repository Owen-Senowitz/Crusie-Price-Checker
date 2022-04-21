from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from twilio.rest import Client

sid = 'AC821e03ec2344682cba70a1b7e9a72061'
authToken = 'authToken'
baseurl = "https://www.royalcaribbean.com/booking/landing?packageCode=EX06W131&groupId=EX06MIA-638683774&sailDate=2022-05-08&shipCode=EX&destinationCode=CARIB&selectedCurrencyCode=USD"
client = Client(sid, authToken)


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))
driver.get(baseurl)
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
price = soup.find('span', {'class': 'pricing-promotions__price-value'})
print('$' + price.text)
message = client.messages.create(
    to='+19196326259',
    from_='+12543281783',
    body='Crusie amount is: $' + price.text
)
driver.close()
