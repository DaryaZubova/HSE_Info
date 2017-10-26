import requests
from bs4 import BeautifulSoup

wiki_url = 'https://mo.wikipedia.org'
url = 'https://mo.wikipedia.org/wiki/Ислам'
req = requests.get(url)

soup = BeautifulSoup(req.text, 'lxml')

all_hrefs = list(map(lambda x: x.get('href'), soup.findAll('a')))
all_hrefs = list(filter(lambda x: x is not None, all_hrefs))

relative_hrefs = list(filter(lambda x: x.startswith('http') is False, all_hrefs))
fixed_hrefs = list(map(lambda x: wiki_url + x, relative_hrefs))

absolute_hrefs = list(filter(lambda x: x.startswith('http') is True, all_hrefs))

hrefs = []
hrefs.extend(fixed_hrefs)
hrefs.extend(absolute_hrefs)

hrefs = list(set(hrefs))
