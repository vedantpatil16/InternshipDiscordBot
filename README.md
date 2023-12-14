# Discord Bot - (Archive Version)
This repository contain archived versions of [Bot Name], a Discord bot developed in Python for enhancing user interactions and automating tasks within Discord servers.

This version is no longer maintained or actively developed. Refer to the main repository for the latest updates and features.

## Installation
1. Clone the repository to your local machine.
2. Install the required Python libraries by using pip install module_name
3. Obtain the necessary API keys and tokens for Discord and Google APIs.
4. Run the files using Python by executing the files: `python FILENAME.py

## Contents
The archive includes multiple Python code files, focusing and having specific functionalities:
- **[FinalDisordBot1.py]**: This file contains all the functionalities invoked by '/news' command such as homepage, upcoming events, Latest news across various federations and Clear button. 
		The variation is for the posting of news articles. When posting on a discord server the bot will post the latest 4 news from the respective federation. The bot will post 4 embeds for 4 news articles, each embed will contain title of news, link of news and thumbnail of news set as image.	  
- **[File Name 2]**: Functionality description or brief explanation.
- **[File Name 3]**: Functionality description or brief explanation.

## Feature specific files
**[ButtonDiscord.py]**: This file is used for demonstration of buttons and interactions with the user in discord.

**[CalenderDiscordBot1.py]**: After giving '/news' command on the server this bot will post the upcoming ISSF events for that current month only. Only the events having start date after/on the current day will be posted.
 **[CalenderDiscordBot2.py]**: After giving '/news' command on the server this bot will ask two options Upcoming events and Latest news. A demo button named 'Click me' would appear that would give message as 'This interaction failed' as the button is not handled.  
			       1) Clicking Upcoming_events button would post the next 5 events.
			       2) Clicking Latest news button would ask you for choosing the federation.This program contains only 1 federation as ISSF. Another button in this view would be homepage which is not handled and would produce no result on clicking.
**[CalenderDiscordBot3.py]**: After giving '!event()' command the program would post the upcoming events for that current month which are scheduled for after/on the current day.

**[ClearMessage.py]**: This program file is created to focus on single command (button) i.e. '/clear'. In this code the logic for clearing the messages in a server channel is developed.

**[edgecase.py(1-2)]**: This programs are developed to handle the year change edge case. If we need to fetch the next 5 upcoming events in December then its necessary that our bot considers the next January and give us the respective events.

**[DateIncrement.py]**: This program file is created for the demonstration of incrementing the month and date as per need.

**[USAshooting.py]**: This program file will is used to scrap the USA Shooting Federation website and print the latest on our standard output console. This program is not attached to the discord.
**[USAshooting2.py]**: After giving the command on discord server as '/usa' it post latest news messages on the discord server.

**[EuropeanShooting.py]**: After giving the command as '/esc' on server this program will scrap the European Shooting Website and post the latest news from the website.

**[GoogleMaps(1-4).py]**: These files are the attempt made to scrap the data from a customised google map and post the relevant information on the discord server channel.

**[NRAI.py]**: This program is demonstrtion to scrap the National Rifle Association of India website and get the latest updates and news from the website that is in text format. The NRAI is not integrated with our main project as of 14/12/2023.

**[SeleniumDemo.py]**: This program is developed to dynamically change the year by actually clicking the dropdown year list and then collecting the respective data by changing the year.

**[WebsiteScrap(1-3).py]**: These 3 programs are just for the demonstration of web scrapping of ISSF website.
