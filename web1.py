from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen('http://www.pythonscraping.com/pages/page1.html')
#bs = BeautifulSoup(html.read(), 'html5lib')
# print(bs.h1)
from urllib.error import URLError
from urllib.error import HTTPError
# try:
    # html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
# except HTTPError as e:
    # print(e)
# except URLError as e:
    # print('The server could not be found!')
# else:
    # print('It Worked!')
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bs = BeautifulSoup(html.read(), 'html.parser')
		title = bs.body.h1
	except AttributeError as e:
		return None
	return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title == None:
	print('Title could not be found')
else:
	print(title)