from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.error import HTTPError

# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
# nameList = bs.findAll('span', {'class':'red'})
# for name in nameList:
	# print(name.get_text())
	
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
	# print(sibling)
	
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',
	{'src':'../img/gifts/img1.jpg'})
	.parent.previous_sibling.get_text())