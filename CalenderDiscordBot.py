import feedparser
import requests
import bs4
from bs4 import BeautifulSoup
import datetime
from datetime import date

url = "https://www.issf-sports.org/calendar/international_championships.ashx"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}

res = requests.get(url,headers=headers)

mont = datetime.datetime.now().month
curmonth = f"monthcship_1"

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    counter = 0
    soupext = soup.find("div",class_="cship-wrapper collapse",id="monthcship_11")
    for events in soupext:
        event_name = events.find('div', class_="title").text.strip()
        event_date = events.find('div', class_="date").text.strip()
        event_venue = events.find('div', class_="city").text.strip()

        atag = events.find('a')
        href = atag.get('href')
        counter = counter+1
        print(f"Name : {event_name}, City : {event_venue}, Date : {event_date}")
        print()
        print("https://www.issf-sports.org/"+href)
    
    if (counter < 3):
        extra = soup.find("div",class_="cship-wrapper collapse",id="monthcship_12")
        for events in extra:
            if(counter < 3):
                event_name = events.find('div', class_="title").text.strip()
                event_date = events.find('div', class_="date").text.strip()
                event_venue = events.find('div', class_="city").text.strip()

                atag = events.find('a')
                href = atag.get('href')
                counter = counter+1
                print(counter)
                print(f"Name : {event_name}, City : {event_venue}, Date : {event_date}")
                print()
                print("https://www.issf-sports.org/"+href)

#webhook_url = "https://discord.com/api/webhooks/1170954159596523520/-idTcR_adj3-6jmDOLoza8w2o_69kKK3429QQ4_-WmcoilSQNi-g1fHaxvcJvscmeHP5"
#message = "ISSF has posted a news : "+ blog_feed.entries[0].title +"                    "+blog_feed.entries[0].link 


#data = {"content": message}
#response = requests.post(webhook_url, json=data)

#if response.status_code == 204:
    #   print("Message sent successfully")
#else:
    #   print(f"Failed to send message. Status code: {response.status_code}")

