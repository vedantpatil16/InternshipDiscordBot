import requests
from bs4 import BeautifulSoup
import itertools
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Path to your ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Initialize Chrome driver
driver = webdriver.Chrome()
# Make a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}
url = 'https://www.google.com/maps/d/u/0/viewer?mid=11V95vnA00cdHvHy1wq2asAIp2TIQbaE&ll=18.866494725244202%2C75.55838825000002&z=5'  # Replace with the URL of the website
response = requests.get(url,headers=headers)
# Open the website
driver.get(url)

dropdown = driver.find_element(By.ID,'layer 0')
dropdown.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'HzV7m-pbTTYe-bN97Pc')))
cont = driver.find_element(By.CLASS_NAME, 'HzV7m-pbTTYe-bN97Pc')
soup = BeautifulSoup(driver.page_source, 'html.parser')
outer_cont = soup.find("div",class_="HzV7m-pbTTYe-bN97Pc")
for i in range(0,3):
    cont = outer_cont.find("div",class_="HzV7m-pbTTYe-ibnC6b pbTTYe-ibnC6b-d6wfac",index=0,subindex=i)
    print(cont)