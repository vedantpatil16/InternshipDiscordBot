import requests
from bs4 import BeautifulSoup
import itertools
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") 
# Path to your ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)
# Make a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}
url = 'https://www.google.com/maps/d/u/0/viewer?mid=11V95vnA00cdHvHy1wq2asAIp2TIQbaE&ll=18.866494725244202%2C75.55838825000002&z=5'  # Replace with the URL of the website
response = requests.get(url,headers=headers)
# Open the website
driver.get(url)

#WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'HzV7m-b0t70b-haAclf HzV7m-b0t70b-bnBfGc HzV7m-b0t70b-ZiwkRe')))

cont = driver.find_element(By.ID, 'legendPanel')
cont2 = cont.find_element(By.CLASS_NAME,'i4ewOd-PBWx0c-bN97Pc-haAclf')
cont3 = cont2.find_element(By.CLASS_NAME,'HzV7m-pbTTYe')
cont4 = cont3.find_element(By.CLASS_NAME,'HzV7m-pbTTYe-SmKAyb-haAclf')
cont5 = cont4.find_element(By.CLASS_NAME,'HzV7m-pbTTYe-KoToPc-ornU0b')
#dropArrow = cont5.find_element(By.CLASS_NAME,'uVccjd HzV7m-pbTTYe-KoToPc-ornU0b-hFsbo HzV7m-KoToPc-hFsbo-ornU0b').below({By.CLASS_NAME: 'HzV7m-pbTTYe-KoToPc-ornU0b'})
#dropArrow.click()
dropdown = driver.find_element(By.ID,'layer 0')
dropdown.click()
#driver.execute_script("arguments[0].setAttribute('aria-checked', 'true');", dropdown)
dropArrow = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.CSS_SELECTOR, '.uVccjd.HzV7m-pbTTYe-KoToPc-ornU0b-hFsbo.HzV7m-KoToPc-hFsbo-ornU0b'))
)
dropdown.click()
dropArrow.click()
#driver.execute_script("arguments[0].setAttribute('aria-checked', 'true');", dropArrow)
#print(dropArrow.get_attribute('aria-checked'))
print(dropdown.is_selected())
element = driver.find_element(By.CLASS_NAME,"HzV7m-pbTTYe-JNdkSc-PntVL")

element = element.find_element(By.CLASS_NAME,"suEOdc")
print(element.get_attribute('data-tooltip'))

#cont = driver.find_element(By.CLASS_NAME,'HzV7m-pbTTYe-bN97Pc HzV7m-pbTTYe-bN97Pc-qAWA2')

is_clickable = element.is_enabled() and element.is_displayed()

print(is_clickable)
#element.click()
element.click()

#WebDriverWait(driver, 300).until(
 # EC.presence_of_element_located((By.CSS_SELECTOR, '.HzV7m-b0t70b-haAclf HzV7m-b0t70b-bnBfGc HzV7m-b0t70b-ZiwkRe'))
#)

soup = BeautifulSoup(driver.page_source, 'html.parser')
container = soup.find('div',class_="qqvbed-UmHwN")
i = 0
for cont in container:
    if i == 2:
        print(cont.text)
        break
    else:
        i += 1

driver.quit()

#rangesContainer = outer_cont[index].find("div",class_="HzV7m-pbTTYe-JNdkSc-PntVL HzV7m-pbTTYe-JNdkSc-L6cTce")
#for i in range(0,len(rangesContainer)):
    #ranges = rangesContainer.find("div",class_="HzV7m-pbTTYe-ibnC6b pbTTYe-ibnC6b-d6wfac",index=index,subindex=i)
    #print(ranges.text)