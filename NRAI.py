import requests
from bs4 import BeautifulSoup
import itertools

# Make a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}
url = 'https://www.thenrai.in/news_events_details.aspx'  # Replace with the URL of the website
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
container = soup.find("table")
content = container.find("div",class_="div_events")
title = content.find('h1')
print(title.text)
link = content.find('a',target='_blank')
print(link['href'])
print()
print()
print()

content = container.find_all("div",class_="div_events")
for i in range(0,3):
    
    print(content[i])
    print()
    print()