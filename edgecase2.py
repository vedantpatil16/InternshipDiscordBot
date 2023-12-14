import requests
from bs4 import BeautifulSoup
import copy

# Make a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}
url = 'https://www.issf-sports.org/calendar/international_championships.ashx'  # Replace with the URL of the website
response = requests.get(url,headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
# Find the span by ID
divog = soup.find('div',class_="calendar-list-wrapper")
#span_element = div_container.find("span",id="ctl00_cphMainContent_issfViewControler_ctl01_ctl00_lYearText")

#ctl00_cphMainContent_issfViewControler_ctl01_ctl00_lYearText
#if span_element:
    # Update the text of the span
    #span_element.string = '2024'  # Set the value to 2024

    # Scraping the updated content of the span
    #updated_content = span_element.text.strip()
    
    # Print or process the updated content
    #print("Updated content:", updated_content)
#else:
    #print("Span with the specified ID not found")

#finalelement = soup.find("div",class_="col-5 currentyear")
#print(div_container)
#print(finalelement)
if divog:
    option_target = divog.find('option',{'value':'2024'})
    option_curr = divog.find('option',{'selected':'selected'})
    option_curr.string = "2024"
    option_curr["value"] = "2024"

    span_element = divog.find("span",id="ctl00_cphMainContent_issfViewControler_ctl01_ctl00_lYearText")
    span_element.string = "2024"


#option_tags.string = '2024'
#option_tags['value'] ='2024'
#soup.extend(option_tags)
print(option_curr)
divelement = divog.find("select",class_="form-control form-control-sm")
print(divelement)
divelement = divog.find("div",class_="col-5 currentyear")
print(divelement)
#div = soup.find('div',class_="calendar-list-wrapper")
#print(div)


#<div class="monthheader" data-toggle="collapse" href="#monthcship_1" role="button" aria-expanded="true" aria-controls="collapseExample">January</div>