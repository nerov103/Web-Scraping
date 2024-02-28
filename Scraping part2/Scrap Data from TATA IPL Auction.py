#Web Scraping Import library in python
import requests
from bs4 import BeautifulSoup
import pandas as pd


#this us scraping url
url = 'https://www.iplt20.com/auction'

#making a requests
reques = requests.get(url)
# print(reques) >> (Test in server responce)

#use beautifulsoup
supe = BeautifulSoup(reques.text, 'lxml')
# print(supe.text)

#get table class
all_table_tag = supe.find('table', class_ = 'ih-td-tab auction-tbl')
# print(all_table_tag) >>>(get all table tag)

#table th 
table_head = all_table_tag.find_all('th')
# print(table_head) >>> (get table class)

title = []
for i in table_head:
    tbl = i.text
    title.append(tbl)

# print(title) >>>(get table head data)

table_rows = all_table_tag.find_all('tr')
# print(table_rows)

#Emtry List
headers = [hed.text for hed in all_table_tag.find_all('th')]
df = pd.DataFrame(columns=headers)

#Creating A For loop
for x in table_rows[1:]:
    tels = x.find_all('td')[0].find('div', class_ = 'ih-pt-ic').text.strip()
    data_td = x.find_all('td')[1:]
    row = [ch.text for ch in data_td]
    # print(row)get all data 
    row.insert(0, tels)
    My_ver = len(df)
    df.loc[My_ver] = row
print(df)

#data in save to csv formet
df.to_csv('t20_stock_data_2023.csv')

















