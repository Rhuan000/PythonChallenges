import bs4
import requests


response = requests.get("https://news.ycombinator.com/")
we_page = response.text

soup = bs4.BeautifulSoup(we_page, "html.parser")
articles = soup.find_all(name='span', class_="titleline")
articles_text = []
articles_link = []

for article_tag in articles:
    text = article_tag.get_text()
    articles_text.append(text)
    link = article_tag.find('a').get('href')
    articles_link.append(link)


article_votes = [int(scores.get_text().split(' ')[0]) for scores in soup.find_all(name="span", class_="score")]
index_maxvotes = article_votes.index(max(article_votes))

print(articles_text[index_maxvotes])
print(articles_link[index_maxvotes])
print(article_votes[index_maxvotes])