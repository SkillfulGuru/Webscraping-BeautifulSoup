from bs4 import BeautifulSoup
import requests

url = 'http://www.pythonscraping.com/pages/page3.html'
# get contents from url
content = requests.get(url).content
# get soup
soup = BeautifulSoup(content,'lxml') # choose lxml parser
# find the tag : <img ... >
image_tags = soup.findAll('img')
# print out image urls
for image_tag in image_tags:
    print(image_tag.get('src'))
