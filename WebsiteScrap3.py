import bs4
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}

res = requests.get("https://www.issf-sports.org/news.ashx?newsid=4091",headers=headers)

print(type(res))

print(res.text)

soup = bs4.BeautifulSoup(res.text,'lxml')
print(type(soup))

title = soup.select('title')
print(title[0].getText())

print("Title is ")
print(title[0].getText())

arr = soup.select(".mw-headline")

for element in arr:
  print(element.text)
