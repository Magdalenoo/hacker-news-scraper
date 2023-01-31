import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# Creates an object that can be manipulated
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

total_link = links + links2
total_subtext = subtext + subtext2

def sort_story(news_list):
    return sorted(news_list, key= lambda k:k['votes'], reverse=True)

def custom_news(links, subtext):
    news = []
    # We need to enumerate links, otherwise we won't get access to votes
    for count, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[count].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                news.append({'title': title, 'link': href, 'votes': points})
    return sort_story(news)

pprint.pprint(custom_news(total_link, total_subtext))