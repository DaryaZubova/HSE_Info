import requests
from bs4 import BeautifulSoup
from IPython.display import HTML, display

max_number = 34673
i = -1
counter = 0

while counter < 1000:
    i += 1
    number = max_number - i
    url = 'http://www.resbash.ru/news/{}'.format(str(number))
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')

    # TEXT
    try:
        text_list = list(map(lambda x: x.text, soup.find('div', attrs={'style': 'padding:10px 20px;font-size:13px;display:inline;'}).findAll('p')))
        text = '\n'.join(text_list)
    except:
        continue

    # TOPIC
    topic = soup.findAll('a', attrs={'class':'a_dec'})[0].text

    # DATE
    date = soup.find('div', attrs={'style': 'border-bottom:2px solid #216594;padding:6px 10px 3px 10px;background:#DDE6F5;font-size:14px;'}).text.strip()[:8]

    # AUTHOR
    author = soup.findAll('a', attrs={'class':'a_14a'})[1].text[7:]

    # TITLE
    title = soup.findAll('title')[0].text

    to_save = "{author}\n{title}\n{date}\n{topic}\n{url}\n{text}".format(author=author, title=title,
                                                                         date=date, topic=topic,
                                                                         url=url, text=text)

    # save to file
    with open('posts/{}.txt'.format(number), 'w') as f:
        f.write(to_save)
        counter += 1
        print('Done with {}, counter={}'.format(number, counter))
