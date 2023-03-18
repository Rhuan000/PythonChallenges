import bs4
import requests

'''with open('website.html') as data:
    contents = data.read()

soup = bs4.BeautifulSoup(contents, 'html.parser')
all_anchor_tag = soup.find_all(name='a')
heading = soup.find(name='h1', id='name')

for tag in all_anchor_tag:
    print(tag.get_text())
    print(tag.get('href'))
print(heading)

company_url = soup.select(selector="p a")
print(company_url)'''

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