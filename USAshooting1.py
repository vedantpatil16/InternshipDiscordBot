import requests
from bs4 import BeautifulSoup
import itertools

# Make a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}
url = 'https://usashooting.org/news/category/news-and-press/'  # Replace with the URL of the website
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
container = soup.find("div",class_="blog-block col-12 col-md-6 col-lg-12 col-xl-6")
title = container.find("p",class_="post-title")
img = container.find("div",class_="bg-img")
#print(title.text)
img = (img['style'])
img = (img[16:]).rstrip(",')")
#print(img)

link = container.find("a",class_="block-inner row g-0 white-background")
#print(link['href'])


outer_container = soup.find("div",class_="plp-row row g-0")
title = outer_container.find_all("p",class_="post-title")
link = outer_container.find_all("a",class_="block-inner row g-0 white-background")
date = outer_container.find_all("span",class_="date col-auto")

for (titles,links,date,i) in zip (title,link,date,range(0,4)):
    print(titles.text)
    print(links['href'])
    print(date.text)
    print(i)

for title in title:
    print(title.text)
img = outer_container.find_all("div",class_="bg-img")
for img in img:
    img = img['style']
    img = (img[16:]).rstrip(",')")
    print(img)
link = outer_container.find_all("a",class_="block-inner row g-0 white-background")
for links in link:
    print(links['href'])
