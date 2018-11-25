# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

myurl = 'https://www.nzx.com/markets/NZSX'
myweb_data = requests.get(myurl)
myweb_data.encoding = 'utf-8'
mysoup = BeautifulSoup(myweb_data.text, 'html.parser')

file = open("resp_text.html", "w+", encoding="utf-8")
file.write(myweb_data.text)
file.close()