import requests
import bs4
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import datetime
from datetime import date

intents = discord.Intents.default()
intents.message_content = True

url = "https://www.issf-sports.org/calendar/international_championships.ashx"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}

# Create a bot instance
bot = commands.Bot(command_prefix='/',intents=intents)

# Define an event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Define a simple command
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your bot!')

@bot.command()
async def news(ctx):
    res = requests.get(url,headers=headers)

    mont = datetime.datetime.now().month
    curmonth = f"monthcship_{mont}"
    print(curmonth)
    if res.status_code == 200:
        soup = soup = BeautifulSoup(res.text, 'html.parser')
        events_container = soup.find("div", class_="cship-wrapper collapse show", id=curmonth)
        i = 1
        for events in events_container:
            event_name = events.find('div', class_="title").text.strip()
            event_date = events.find('div', class_="date").text.strip()
            event_venue = events.find('div', class_="city").text.strip()
            
            today_date = datetime.datetime.now().strftime("%d.%m")
            start_date_str, end_date_str = event_date.split(" - ")

            start_date = datetime.datetime.strptime(start_date_str, "%d.%m")
            today_date = datetime.datetime.strptime(today_date, "%d.%m")
            atag = events.find('a')
            href = atag.get('href')
            bot_response = []
            if(today_date <= start_date):
                strtosend = f"{i}) Name : {event_name}, City : {event_venue}, Date : {event_date}, Link : https://www.issf-sports.org/+href"
                bot_response.append(strtosend)
                i=i+1
                await ctx.send(strtosend)

            


# Run the bot with your token
bot.run('MTE3MTcxNTIyMDk0Nzg3MzgzMw.GKEFVG.6OvzsLU9Edar4EjU2VW6QQdakoynFRdlqx2X4w')
