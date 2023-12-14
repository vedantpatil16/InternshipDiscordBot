import requests
import feedparser

rss_url = "https://www.issf-sports.org/news_multimedia/newslist.ashx"


feed = feedparser.parse(rss_url)
print(feed.entries[0].content)

listmessage = []
if feed.bozo == 0:
    for entry in feed.entires:
        title = entry.title
        content = entry.content[0].value if 'content' in entry else entry.summary
        listmessage.append((title,content))

for title, content in listmessage:
    print("Title:", title)
    print("Content:", content)
    print()   

print(listmessage)
#webhook_url = "https://discord.com/api/webhooks/1170954159596523520/-idTcR_adj3-6jmDOLoza8w2o_69kKK3429QQ4_-WmcoilSQNi-g1fHaxvcJvscmeHP5"
#message = "This is a news update from ISSF."
#print(message)
#data = {"content": message}
#response = requests.post(webhook_url, json=data)

#if response.status_code == 204:
 #   print("Message sent successfully")
#else:
 #   print(f"Failed to send message. Status code: {response.status_code}")