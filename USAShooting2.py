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
async def usa(ctx):
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }
    url = 'https://usashooting.org/news/category/news-and-press/'  # Replace with the URL of the website
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    embed = []
    outer_container = soup.find("div",class_="plp-row row g-0")
    title = outer_container.find_all("p",class_="post-title")
    link = outer_container.find_all("a",class_="block-inner row g-0 white-background")
    img = outer_container.find_all("div",class_="bg-img")
    for (titles,links,i,imgs) in zip (title,link,range(0,4),img):

            match i:
                case 0:
                    color = discord.Color.blue()
                case 1:
                    color = discord.Color.red()
                case 2:
                    color = discord.Color.green()
                case 3:
                    color = discord.Color.yellow()

            img = imgs['style']
            img = (img[16:]).rstrip(",')")
            embed1 = discord.Embed(title=titles.text,
                        description=links['href'],
                        color=color)
            
            embed1.set_image(url=img)
            await ctx.send(embed=embed1)
            
# Run the bot with your token
bot.run('MTE3MTcxNTIyMDk0Nzg3MzgzMw.GKEFVG.6OvzsLU9Edar4EjU2VW6QQdakoynFRdlqx2X4w')
