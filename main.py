import os
import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/OnePlus-Moonstone-Smartphone-SuperVOOC-CPH2417/dp/B0B7QQN6P9/?_encoding=UTF8&pd_rd_w=XE0mq&content-id=amzn1.sym.595f69d1-9647-4ce9-9fca-a43eb1c1f3b6&pf_rd_p=595f69d1-9647-4ce9-9fca-a43eb1c1f3b6&pf_rd_r=3XCX5P3DM32GRHVN8NX1&pd_rd_wg=s5DsZ&pd_rd_r=81a189cd-309d-423f-8c85-0dcca5c355a4&ref_=pd_gw_exports-popular-this-season-with-similar-asins%2F&th=1"
product_name = URL.split("/")[3]

ACCEPT_LANGUAGE = os.environ.get("Accept-Language")
USER_AGENT = os.environ.get("User-Agent")
ACCEPT = os.environ.get("Accept")
SENDER = os.environ.get("sender")
RECIVER = os.environ.get("reciver")
APP_PASS = os.environ.get("app_pass")

header = {
    "Accept-Language":ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT,
    "Accept": ACCEPT
}

r = requests.get(URL, headers=header).text
soup = BeautifulSoup(r, "html.parser")
prices = soup.find(
    "span", class_="a-price-whole").text

price = int(prices.replace('.', ''))

ideal_price = 500
if price < ideal_price:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=SENDER, password=APP_PASS)
    connection.sendmail(from_addr=SENDER, to_addrs=RECIVER,
                        msg=f"subject : Price Alert for {product_name}\n\n {product_name} is now ${price}\n{URL}"
                        )
    connection.close()
    print("email sent")

