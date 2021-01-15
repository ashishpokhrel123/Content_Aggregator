import requests
from bs4 import BeautifulSoup

# from TechCruch
 r = requests.get('https://techcrunch.com/startups/')
 soup = BeautifulSoup(r.content, 'html5lib')
 print(soup)