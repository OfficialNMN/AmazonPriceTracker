import requests
from bs4 import BeautifulSoup

import smtplib

Url='https://www.amazon.in/TCL-79-97cm-inches-Ready-Android/dp/B07MD8RJW3/ref=sr_1_2?dchild=1&keywords=tcl+32+inch+smart+led+tv+full+hd&qid=1600242012&sr=8-2'

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}


page=requests.get(Url,headers=headers)
soup=BeautifulSoup(page.content,'html.parser')

def check_price():
	title=soup.find(id='productTitle').get_text().strip()
	price=soup.find(id='priceblock_ourprice').get_text()[2:8]
	converted_price=float(price.replace(",",""))
	print(title)
	print(converted_price)
	#if converted_price<15500:
		#send_mail()
	
check_price()