# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import datetime

myurl = 'https://www.nzx.com/markets/NZSX'

myweb_data = requests.get(myurl)
myweb_data.encoding = 'utf-8'
mysoup = BeautifulSoup(myweb_data.text, 'lxml')

stuff = mysoup.find('table', {'id': 'instruments-table'})

# extract instrument names
stuff2 = stuff.findAll('a')
for i in range(0,len(stuff2)):
	stuff2[i] = stuff2[i].text.strip()

_length = int(len(stuff2)/2)
for i in range(0,_length):
	del stuff2[i]

# extract prices
prices = mysoup.findAll('td', {'data-title':'Price'})
for i in range(0,len(stuff2)):
	prices[i] = prices[i].text.strip()

# extract instrument name abbreviations	
abv = stuff.findAll('strong')
for i in range(0,len(stuff2)):
	abv[i] = abv[i].text.strip()

# create empty list
_list = [None] * len(stuff2)

# combine each instrument name, abbreviation and price into one list
for i in range(0,len(stuff2)):
	stringy = "{0}  {1}   {2}".format("%-5s" % abv[i], "%-60s" % stuff2[i], "%-8s" % prices[i])
	_list[i] = stringy

# sort the list alphabetically
_list.sort()

# display list
for i in sorted(_list):
	print(i)
	print("")
