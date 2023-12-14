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
    my_task.start()

#async def create_button():
 #   view = ButtonView()
  #  buttons_data = [
   #     {"label": "Command 1", "command": "!command1"},
    #    {"label": "Command 2", "command": "!command2"},
        # Add more buttons as needed
    #]

    #for button_info in buttons_data:
     #   button = Button(style=discord.ButtonStyle.primary, label=button_info["label"])
      #  button.callback = button_callback
       # button.custom_id = button_info["command"]
        #view.add_item(button)

    #channel_id = 1171754867480604736
    #channel = bot.get_channel(channel_id)
    #if channel:
     #   message = await channel.send("Click a button to execute a command:", view=view)

#class ButtonView(View):
 #   def __init__(self):
  #      super().__init__()

   # async def on_timeout(self):
        # Cleanup after the view times out (buttons disappear)
    #    for item in self.children:
     #       if isinstance(item, Button):
      #          item.disabled = True

#async def button_callback(button, interaction):
 #   # Get the command associated with the button
  #  command = interaction.data["custom_id"]

    # Invoke the command
   # await bot.process_commands(bot.message_listeners[interaction.message.id].message)
    
    # Remove the interaction
    #await interaction.response.defer()

@tasks.loop(minutes=1.0) 
async def my_task():
    global target_datetime
    global buffer_time
    current_time = datetime.datetime.now()
    
    if (current_time >= target_datetime and current_time <= buffer_time):
        print(datetime.datetime.now())
        task_inc = datetime.datetime.now().minute
        task_inc = task_inc+5
        target_datetime = target_datetime + relativedelta(minutes=5)
        buffer_time = buffer_time + relativedelta(minutes=5)
        print(target_datetime)
        print(buffer_time)
        channel_id = 1171754867480604736
        channel = bot.get_channel(channel_id)

        if channel:
            res = requests.get(url,headers=headers)

            mont = datetime.datetime.now()
            extra_month = mont + relativedelta(months=1)

            curmonth = f"monthcship_{mont.month}"
            extramon = f"monthcship_{extra_month.month}"
            print(extramon)

            if res.status_code == 200:
                soup = soup = BeautifulSoup(res.text, 'html.parser')
                events_container = soup.find("div", class_="cship-wrapper collapse show", id=curmonth)
                extra_container = soup.find("div", class_="cship-wrapper collapse", id=extramon)
                i = 1
                for events in events_container:
                    event_name = events.find('div', class_="title").text.strip()
                    event_date = events.find('div', class_="date").text.strip()
                    event_venue = events.find('div', class_="city").text.strip()
                    atag = events.find('a')
                    href = atag.get('href')
                    pre_href = "https://www.issf-sports.org/"
                    final_href = pre_href + href
                    strtosend = f"{i}) Name : {event_name}, City : {event_venue}, Date : {event_date}, Link : {final_href}"
                    i=i+1
                    await channel.send(strtosend)

                print(extra_container)
                for events in extra_container:
                    event_name = events.find('div', class_="title").text.strip()
                    event_date = events.find('div', class_="date").text.strip()
                    event_venue = events.find('div', class_="city").text.strip()
                    atag = events.find('a')
                    href = atag.get('href')
                    pre_href = "https://www.issf-sports.org/"
                    final_href = pre_href + href
                    strtosend = f"{i}) Name : {event_name}, City : {event_venue}, Date : {event_date}, Link : {final_href}"
                    i=i+1
                    await channel.send(strtosend)
        
    

@bot.command()
async def news(ctx):
    embed = discord.Embed(title="Hi, I'm ProshooterVR Bot!",
                          description="I am a bot for shooting sports, etc.",
                          color=discord.Color.blurple())

    embed.add_field(name="Click here to do something",
                    value="Replace this with what you want the link to do.",
                    inline=False)

    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/161875352992481281/a_c3eb7cafec0e5928fe7d869e9e47eac0.gif?size=1024")
    view = SimpleView()
    button = discord.ui.Button(label="click me")
    view.add_item(button)
    #await ctx.send("You can click below buttons to check for the next upcoming events",view=view)
    await ctx.send(embed=embed,view=view)

class SimpleView(discord.ui.View):
    @discord.ui.button(label="Upcoming_events",style=discord.ButtonStyle.success)
    async def hello(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('event'))
    
    @discord.ui.button(label="Latest News",style=discord.ButtonStyle.blurple)
    async def latest_news(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        #button =[
         #   interaction.ActionRow(
          #      components=[
           #         interactions.Button(
            #            style=interactions.ButtonStyle.PRIMARY,
             #           label="Click me!",
              #          custom_id="click_me",
               #     ),
                #    interactions.Button(
                 #       style=interactions.ButtonStyle.DANGER,
                  #      label="Do not click!",
                   #     custom_id="do_not_click",
                    #),
                #]
            #)
        #]
        await interaction_ctx.invoke(bot.get_command('MultipleNewsOpt'))

class NewsView(discord.ui.View):
    @discord.ui.button(label="Homepage",style=discord.ButtonStyle.blurple,emoji="🏠")
    async def Homepage(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('helpme'))

    @discord.ui.button(label="ISSF",style=discord.ButtonStyle.blurple)
    async def ISSF(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        button.disabled = True
        await interaction_ctx.invoke(bot.get_command('ISSFnews'))
        
# Define a simple command
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your bot!')

@bot.command()
async def MultipleNewsOpt(ctx):
    embed = discord.Embed(title="Latest News",
                         description="Please select a shooting federation whose news you want to view.",
                         )
    view = NewsView()
    await ctx.send(embed=embed,view=view)


@bot.command()
async def ISSFnews(ctx):
    ISSFnewsFeed = feedparser.parse("http://www.issf-sports.org/rss/news.html")
    ISSFnewslist = []
    for i in range(0,3):
        #message = f"{i+1}) {ISSFnewsFeed.entries[i].title}\n{ISSFnewsFeed.entries[i].link}"
        #ISSFnewslist.append(message)
    
    #embed.add_field(name="",value=f"\n".join(ISSFnewslist),inline=False)
        embed1 = discord.Embed(title=ISSFnewsFeed.entries[i].title,
                                description=ISSFnewsFeed.entries[i].link,
                                color=discord.Color.blurple())
        embed1.set_image(url=ISSFnewsFeed.entries[i].links[1].href)
        await ctx.send(embed=embed1)

@bot.command()
async def event(ctx):
    res = requests.get(url,headers=headers)

    mont = datetime.datetime.now().month
    curmonth = f"monthcship_{mont}"
    print(curmonth)
    if res.status_code == 200:
        soup = soup = BeautifulSoup(res.text, 'html.parser')
        events_container = soup.find("div", class_="cship-wrapper collapse show", id=curmonth)
        i = 0
        list_of_events = []
        for events in events_container:
            if(i<5):
                event_name = events.find('div', class_="title").text.strip()
                event_date = events.find('div', class_="date").text.strip()
                event_venue = events.find('div', class_="city").text.strip()
                
                today_date = datetime.datetime.now().strftime("%d.%m")
                start_date_str, end_date_str = event_date.split(" - ")

                start_date = datetime.datetime.strptime(start_date_str, "%d.%m")
                today_date = datetime.datetime.strptime(today_date, "%d.%m")
                atag = events.find('a')
                href = atag.get('href')
                pre_href = "https://www.issf-sports.org/"
                final_href = pre_href+href
                if(today_date < start_date):
                    i=i+1
                    strtosend = f"{i}) Name : {event_name}, City : {event_venue}, Date : {event_date}, Link : {final_href}"
                    list_of_events.append(strtosend)
                    #await ctx.send(strtosend)
        
        if(i<5):
            extramon = datetime.datetime.now() + relativedelta(months=1)
            extramonth = f"monthcship_{extramon.month}"
            extra = soup.find("div",class_="cship-wrapper collapse",id=extramonth)
            for events in extra:
                if(i < 5):
                    event_name = events.find('div', class_="title").text.strip()
                    event_date = events.find('div', class_="date").text.strip()
                    event_venue = events.find('div', class_="city").text.strip()

                    atag = events.find('a')
                    href = atag.get('href')
                    pre_href = "https://www.issf-sports.org/"
                    final_href = pre_href+href
                    i = i+1
                    strtosend = f"{i})Name : {event_name}, City : {event_venue}, Date : {event_date}, Link : {final_href}"
                    #await ctx.send(strtosend)
                    list_of_events.append(strtosend)

        embed = discord.Embed(title="Upcoming Events",
                            description="Here are the next 5 upcoming events",
                            color=discord.Color.blue())

        embed.add_field(name="*ISSF Events*",value="\n".join(list_of_events),inline=False)
        await ctx.send(embed=embed)

# Run the bot with your token
bot.run('MTE3MTcxNTIyMDk0Nzg3MzgzMw.GKEFVG.6OvzsLU9Edar4EjU2VW6QQdakoynFRdlqx2X4w')
