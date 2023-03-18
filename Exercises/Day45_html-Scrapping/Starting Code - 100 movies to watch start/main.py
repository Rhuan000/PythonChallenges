import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

list = soup.find_all(name='h3', class_='title')
just_title = [title.get_text() for title in list]

with open('movies.txt','w') as file:
    for movie in just_title[::-1]:
        file.write(f"{movie}\n")
