import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.de/Raspberry-Pi-ARM-Cortex-A72-Bluetooth-Micro-HDMI/dp/B07TC2BK1X/ref=sr_1_3?crid=2GVGZ9BWADXZ8&dchild=1&keywords=raspberry%2Bpi&qid=1590001020&sprefix=rasberry%2Bpi%2Caps%2C239&sr=8-3&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find(id="productTitle").get_text()
#price = soup.find(id="priceblock_ourprice").get_text()
#converted_price = price[0:5]


print("\n", title, "\n")
#print(price.strip(), "\n")
