# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import datetime

myurl = 'https://www.nzx.com/markets/NZSX/securities/SPK?icharts=true'
myweb_data = requests.get(myurl)
myweb_data.encoding = 'utf-8'
mysoup = BeautifulSoup(myweb_data.text, 'lxml')

_time = datetime.datetime.now().strftime("%d %b %Y %I:%M %p")
name_group = mysoup.find('div', {'class':'small-12 medium-7 columns'})
name = name_group.findAll('td')
share_name = name[1].text.strip()
_isin = name[5].text.strip()

price_group = mysoup.find('div', {'class':'small-12 medium-5 columns'})
price = price_group.find('h1')
share_price = price.text.strip()

high_low = mysoup.find('div', {'class':'small-12 medium-6 large-4 columns'})
strong = high_low.findAll('td', {'class':'text-right'})
_open = strong[0].text.strip()
_high = strong[1].text.strip()
_low = strong[2].text.strip()

print("{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}".format(_time, share_name, "ISIN:  %s" % _isin, "Price: %s" % share_price, "Open:  %s" % _open, "High:  %s" % _high, "Low:   %s" % _low))


# file = open("resp_text2.html", "w", encoding="utf-8")
# file.write(stuff.text)
# file.close()