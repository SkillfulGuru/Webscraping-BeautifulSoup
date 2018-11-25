# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import datetime

myurl = 'https://www.nzx.com/markets/NZSX'

myweb_data = requests.get(myurl)
myweb_data.encoding = 'utf-8'
mysoup = BeautifulSoup(myweb_data.text, 'lxml')

stuff = mysoup.find('table', {'id': 'instruments-table'})
stuff2 = stuff.findAll('a')

for i in range(0,len(stuff2)):
	stuff2[i] = stuff2[i].text.strip()

_length = int(len(stuff2)/2)

for i in range(0,_length):
	del stuff2[i]

print(stuff2)


