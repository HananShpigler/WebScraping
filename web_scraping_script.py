import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
soup_obj = BeautifulSoup(response.text, 'html.parser')
links = soup_obj.select('.titleline > a')
subtext = soup_obj.select('.subtext')
def sort_stories_by_vote(list):
	return sorted(list, key=lambda k:k['votes'], reverse=True)

def create_custom_hacker_news(links, subtext):
	hacker_news_list = []
	for index, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hacker_news_list.append({'title': title, 'link': href, 
				'votes': points})
	return sort_stories_by_vote(hacker_news_list)

pprint.pprint(create_custom_hacker_news(links, subtext))