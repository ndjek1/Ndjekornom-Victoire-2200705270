# Libraries for webscrapping
# Request, BeautifulSoup, lxml, Scrapy, Selenium
# We need API Keys
# Exercises openweathermap.org

# Step 1: import libraries

import requests
from bs4 import BeautifulSoup
import csv
import json

# step 2: Fetch web pages

# url = 'http://ryeko.org'
# response = requests.get(url)
# html_content = response.text


# # Parse html using beautiful soup

# soup = BeautifulSoup(html_content, 'html.parser')

# # Find specific data

# data = [
# ]

# for item in soup.find_all('a'):
#     title = item.text.strip()
#     link = item.get('href')
#     data.append({'title': title, 'link':link})


# csv_file = 'scrapped_data.csv'

# with open(csv_file, mode = 'w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=['title', 'link'])
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)

# json_file = 'scrapped.json'
# with open(json_file, mode = 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii= False, indent=4)

api_key = '02bd50a043cd18936f9bc89d55c664bc'
lat = '0.3163'
lon = '32.5822'
city = 'kampala'
def fetch_forecast():
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q=Kampala,ug&APPID=11aa28f04ba8f7b14efb509309d3da52'
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
data = fetch_forecast()
print(data)