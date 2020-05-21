import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = "https://www.ebay.ca/itm/BenQ-GW2480-24-Full-HD-1920-x-1080-60Hz-5ms-VGA-HDMI-DisplayPort-Flicker-Free-T/182839053967?hash=item2a920e8e8f:g:FVAAAOSwk9pdDKXb"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77"}

password = 'PASSWORD HERE'


def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum").get_text()
    converted_price = float(price[3:9])

    print(title.strip())
    print(converted_price, "\n")

    if converted_price < 150.00:
        sendMail()


def sendMail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('yifan.ding.official@gmail.com', password)

    subject = 'Price Fell Down'
    body = 'Check the ebay link:' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'yifan.ding.official@gmail.com',
        'yifan.ding@berkeley.edu',
        msg
    )
    print('HEY THE EMAIL HAS BEEN SENT')

    server.quit()


while(True):
    checkPrice()
    time.sleep(60*60*24)


checkPrice()
