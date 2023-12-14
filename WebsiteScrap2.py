import feedparser
import requests
url = "http://www.issf-sports.org/rss/news.html"

blog_feed = feedparser.parse(url)
Previous = "ISSF Logo now internationally recognised as an official"

if(Previous != blog_feed.entries[0].title): 
    #print(len(blog_feed))
    #print(blog_feed.entries[0].title) 
    #website_link = blog_feed.entries[1].link 
    #print(website_link)
    #print(blog_feed.entries[0].published) 
    #print(blog_feed)
    #Previous = blog_feed.entries[0].title

    webhook_url = "https://discord.com/api/webhooks/1170954159596523520/-idTcR_adj3-6jmDOLoza8w2o_69kKK3429QQ4_-WmcoilSQNi-g1fHaxvcJvscmeHP5"
    message = "ISSF has posted a news : "+ blog_feed.entries[0].title +"                    "+blog_feed.entries[0].link 

    Previous = blog_feed.entires[0].title

    data = {"content": message}
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")