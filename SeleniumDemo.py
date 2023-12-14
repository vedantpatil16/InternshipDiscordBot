from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Path to your ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Initialize Chrome driver
driver = webdriver.Chrome()

# URL of the website you want to scrape
url = 'https://www.issf-sports.org/calendar/international_championships.ashx'

# Open the website
driver.get(url)

# Find and interact with elements (e.g., clicking on a dropdown to select 2024)
# Replace the following with the actual interaction logic based on the website's structure
# For example, if there's a dropdown with year options:
dropdown = driver.find_element(By.ID,'ctl00_cphMainContent_issfViewControler_ctl01_ctl00_ddlYear')
dropdown.click()
year_2024_option = driver.find_element(By.XPATH,'//option[@value="2024"]')
year_2024_option.click()

# Wait for the page to load or the content you expect to appear
# For example, wait until a specific element is present or visible
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'monthcship_1')))

# Once the desired content is loaded, scrape the data
# For example, find elements containing event information and extract the data
#print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'html.parser')
events_container = soup.find("div", class_="cship-wrapper collapse", id="monthcship_1")
i = 0
list_of_events = []
for events in events_container:
    if(i<5):
        event_name = events.find('div', class_="title").text.strip()
        event_date = events.find('div', class_="date").text.strip()
        event_venue = events.find('div', class_="city").text.strip()

        atag = events.find('a')
        href = atag.get('href')
        pre_href = "https://www.issf-sports.org/"
        final_href = pre_href+href
    
        i=i+1
        strtosend = f"\n{i}) Name : **{event_name}**\nCity : **{event_venue}**\nDate : **{event_date}**\nLink : {final_href}"
        print(strtosend)
# for event in events:
#     event_name = event.find_element_by_class_name('event-name').text
#     event_date = event.find_element_by_class_name('event-date').text
#     print(f"Event: {event_name}, Date: {event_date}")

# Close the browser window
driver.quit()
