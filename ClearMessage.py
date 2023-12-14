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
    embed = discord.Embed(title=f"ProShooterVR Bot|Homepage\n--------------------------",
                          color=discord.Color.blurple())

    embed.add_field(name="Categories",
                    value=f"🏠 Homepage | This page\n\n📅 Upcoming Events | Know about ISSF upcoming events\n\n📰 News | Check the Latest News",
                    inline=False)

    #embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/161875352992481281/a_c3eb7cafec0e5928fe7d869e9e47eac0.gif?size=1024")
    view = SimpleView()

    # Adding buttons to individual action rows
    global user_id
    user_id = ctx.author.id
    #view.add_item(button)
    #await ctx.send("You can click below buttons to check for the next upcoming events",view=view)
    await ctx.send(embed=embed,view=view)

class SimpleView(discord.ui.View):
    @discord.ui.button(label="Upcoming Events",row=0,style=discord.ButtonStyle.primary,emoji="📅")
    async def hello(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('event'))
        #await bot.get_command('event').callback(interaction)

    @discord.ui.button(label="News",style=discord.ButtonStyle.primary,emoji="📰")
    async def latest_news(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        #await interaction_ctx.invoke(bot.get_command('MultipleNewsOpt'))
        await interaction_ctx.invoke(bot.get_command('MultipleNewsOpt'))

class NewsView(discord.ui.View):
    @discord.ui.button(label="Homepage",style=discord.ButtonStyle.blurple,emoji="🏠")
    async def Homepage(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('news'))

    @discord.ui.button(label="ISSF",style=discord.ButtonStyle.blurple,emoji="🗺️")
    async def ISSF(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('ISSFnews'))

    @discord.ui.button(label="USAshooting",style=discord.ButtonStyle.primary,emoji="🇺🇸")
    async def latest_news(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        #await interaction_ctx.invoke(bot.get_command('MultipleNewsOpt'))
        await interaction_ctx.invoke(bot.get_command('usa'))

    @discord.ui.button(label="Upcoming Events",row=0,style=discord.ButtonStyle.primary,emoji="📅")
    async def hello(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('event'))

    @discord.ui.button(label="Clear",style=discord.ButtonStyle.red,emoji="🗑️")
    async def dustbin(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('clear'))
        
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
    for i in range(0,4):
        #message = f"{i+1}) {ISSFnewsFeed.entries[i].title}\n{ISSFnewsFeed.entries[i].link}"
        #ISSFnewslist.append(message)
    
    #embed.add_field(name="",value=f"\n".join(ISSFnewslist),inline=False)
        if(i == 0):
            embed1 = discord.Embed(title=ISSFnewsFeed.entries[i].title,
                                    description=ISSFnewsFeed.entries[i].link,
                                    color=discord.Color.yellow())
            embed1.set_image(url=ISSFnewsFeed.entries[i].links[1].href)
            await ctx.send(embed=embed1)

        if(i == 1):
            embed1 = discord.Embed(title=ISSFnewsFeed.entries[i].title,
                        description=ISSFnewsFeed.entries[i].link,
                        color=discord.Color.blue())
            embed1.set_image(url=ISSFnewsFeed.entries[i].links[1].href)
            await ctx.send(embed=embed1)
        
        if(i == 2):
            embed1 = discord.Embed(title=ISSFnewsFeed.entries[i].title,
                        description=ISSFnewsFeed.entries[i].link,
                        color=discord.Color.dark_green())
            embed1.set_image(url=ISSFnewsFeed.entries[i].links[1].href)
            await ctx.send(embed=embed1)
        
        if(i == 3):
            embed1 = discord.Embed(title=ISSFnewsFeed.entries[i].title,
                                description=ISSFnewsFeed.entries[i].link,
                                color=discord.Color.red())
            view = ISSFNewsHomepage()
            embed1.set_image(url=ISSFnewsFeed.entries[i].links[1].href)
            await ctx.send(embed=embed1,view=view)

class EventHomepage(discord.ui.View):
    @discord.ui.button(label="Homepage",style=discord.ButtonStyle.blurple,emoji="🏠")
    async def Homepage(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('news'))
    
    @discord.ui.button(label="News",style=discord.ButtonStyle.primary,emoji="📰")
    async def latest_news(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        #await interaction_ctx.invoke(bot.get_command('MultipleNewsOpt'))
        await interaction_ctx.invoke(bot.get_command('MultipleNewsOpt'))


    @discord.ui.button(label="Clear",style=discord.ButtonStyle.red,emoji="🗑️")
    async def dustbin(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('clear'))

class USANewsHomepage(discord.ui.View):
    @discord.ui.button(label="Homepage",style=discord.ButtonStyle.blurple,emoji="🏠")
    async def Homepage(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('news'))

    @discord.ui.button(label="ISSF",style=discord.ButtonStyle.blurple,emoji="🗺️")
    async def ISSF(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('ISSFnews'))

    @discord.ui.button(label="Upcoming Events",row=0,style=discord.ButtonStyle.primary,emoji="📅")
    async def hello(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('event'))

    @discord.ui.button(label="Clear",style=discord.ButtonStyle.red,emoji="🗑️")
    async def dustbin(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('clear'))

class ISSFNewsHomepage(discord.ui.View):
    @discord.ui.button(label="Homepage",style=discord.ButtonStyle.blurple,emoji="🏠")
    async def Homepage(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('news'))

    @discord.ui.button(label="USAshooting",style=discord.ButtonStyle.primary,emoji="🇺🇸")
    async def latest_news(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('usa'))
    
    @discord.ui.button(label="Upcoming Events",row=0,style=discord.ButtonStyle.primary,emoji="📅")
    async def hello(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('event'))

    @discord.ui.button(label="Clear",style=discord.ButtonStyle.red,emoji="🗑️")
    async def dustbin(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
        interaction_ctx = await bot.get_context(interaction.message, cls=commands.Context)
        await interaction_ctx.invoke(bot.get_command('clear'))

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
                    strtosend = f"\n{i}) Name : **{event_name}**\nCity : **{event_venue}**\nDate : **{event_date}**\nLink : {final_href}"
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
                    strtosend = f"\n{i})Name : **{event_name}**\nCity : **{event_venue}**\nDate : **{event_date}**\nLink : {final_href}"
                    #await ctx.send(strtosend)
                    list_of_events.append(strtosend)

        embed = discord.Embed(title="Upcoming Events",
                            description="Here are the next 5 upcoming events",
                            color=discord.Color.blue())

        embed.add_field(name="🏆 *ISSF Events* 🏆\n------------------------------------------------------------------------------\n",value="\n".join(list_of_events),inline=False)
        view = EventHomepage()
        await ctx.send(embed=embed,view=view)

@bot.command()
async def clear(ctx):
    # Fetch and delete messages sent by the bot to the specific user
    async for message in ctx.channel.history(limit=None):
        if message.author.id == user_id:
            await message.delete()
            print(message)
            break
        if message.author == bot.user:
            await message.delete()

        #if message.author == user_id:
            #await message.delete()

    #async for message in ctx.channel.history(limit=None):
     #   if message.author.id == user_id:
      #      await message.delete()

    # Optionally, send a confirmation message
    await ctx.send("Bot messages cleared for you.")


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
            embed = discord.Embed(title=titles.text,
                        description=links['href'],
                        color=color)
            
            embed.set_image(url=img)
            view = USANewsHomepage()
            if(i == 3):
                await ctx.send(embed=embed,view=view)
            else:
                await ctx.send(embed=embed)
# Run the bot with your token
bot.run('MTE3MTcxNTIyMDk0Nzg3MzgzMw.GKEFVG.6OvzsLU9Edar4EjU2VW6QQdakoynFRdlqx2X4w')
