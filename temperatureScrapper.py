# import libraries
import requests
import pandas as pd
import csv
import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Climate_of_Dubai'
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.findAll('table', {"class": "collapsible"})[0]
tr = table.findAll(['tr'])[1:11]
csvFile = open("climate.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for cell in tr:
        th = cell.find_all('th')
        th_data = [col.text.strip('\n') for col in th]
        td = cell.find_all('td')
        row = [i.text.replace('\n', '') for i in td]
        writer.writerow(th_data + row)

finally:
    csvFile.close()