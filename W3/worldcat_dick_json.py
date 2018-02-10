import requests
from bs4 import BeautifulSoup
import json
import time


def get_page(s):
	base_url = "http://www.worldcat.org/search?q=ti%3Adick&fq=&dblist=638&start="
	url = base_url + str(s)
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html, "html.parser")
	books = soup.select('.name')

	output = []

	for book in books:
		title = book.select('strong')[0].text
		href = book.select('a')[0].get('href')

		item = {
            'title': title,
            'href': href
        }

		output.append(item)

	return output


start = 1
all_results = []

while start < 5005:
	results = get_page(start)
	all_results = all_results + results
	start = start + 10


outfile = open('dick_books.json', 'w')
json.dump(all_results, outfile, indent=2)
outfile.close()


