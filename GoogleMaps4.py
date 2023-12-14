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
import pandas as pd

# URL of the Google Drive file (make sure it's a direct link to the file)
url = '/home/vedant/Downloads/Google_location_of_the_ranges (1).xlsx'

# Attempt to read the Excel file from the URL
try:
    data = pd.read_excel(url)

    # Filter the data for a specific country (e.g., USA)
    usa_data = data[data['Country'] == 'India']

    # Display the values of ranges and co-ordinates for USA
    print(usa_data[['Name of the Range', 'Google Map Pin Location','Map Link']])
    await ctx.send(usa_data)
except Exception as e:
    print(f"An error occurred: {e}")