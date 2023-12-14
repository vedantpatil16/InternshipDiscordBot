import requests
import bs4
from bs4 import BeautifulSoup
import discord
from discord.ext import commands, tasks
from discord.ui import Button, View
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import asyncio 
import feedparser
#import disnake

intents = discord.Intents.default()
intents.message_content = True

url = "https://www.issf-sports.org/calendar/international_championships.ashx"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}

target_datetime = datetime.datetime(2023, 11, 9, 13, 40, 0)
buffer_time = datetime.datetime(2023, 11, 9, 18, 45, 0)

# Create a bot instance
bot = commands.Bot(command_prefix='/',intents=intents)

# Define an event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def esc(ctx):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }
    url = 'https://esc-shooting.org/news/'  # Replace with the URL of the website
    response = requests.get(url,headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    news_container = soup.find("div",class_="latest_news")
    link = news_container.find("a")
    link = "https://esc-shooting.org"+link['href']
    img = news_container.find("img")
    img = "https://esc-shooting.org"+img['src']
    title = news_container.find("span",class_="title")
    title = title.text
    print(news_container)
    embed = discord.Embed(title=title,
                        description=link,
                        color=discord.Color.gold())

    embed.set_image(url=img)

    await ctx.send(embed=embed)

    content = news_container.find("div",class_="right_side")
    link = content.find_all("a")
    img = content.find_all("img")
    title = content.find_all("span",class_="title")
    print(content)
    for(link,img,title,i) in zip(link,img,title,range(0,3)):

        Title = title.text
        Img = img['src'].strip()
        Img = "https://esc-shooting.org"+Img
        Link = "https://esc-shooting.org"+link['href'].strip()
        print(Img)
        embed1 = discord.Embed(title=Title,
                    description=Link,
                    color=discord.Color.gold())
            
        embed1.set_image(url=Img)
        await ctx.send(embed=embed1)
            
# Run the bot with your token
bot.run('MTE3MTcxNTIyMDk0Nzg3MzgzMw.GKEFVG.6OvzsLU9Edar4EjU2VW6QQdakoynFRdlqx2X4w')
