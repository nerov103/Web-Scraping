import requests
from bs4 import BeautifulSoup
import pandas as pd

#create your own function
url = 'https://ticker.finology.in/'
req = requests.get(url)
supe = BeautifulSoup(req.text, 'lxml')

data_tabel = supe.find('table', class_ = 'table table-sm table-hover screenertable')
# data_table_th = data_tabel.find_all('th')

# tbhead = []
# for i in data_table_th:
#     title = i.text
#     tbhead.append(title)
# ped = pd.DataFrame(columns=tbhead)

#extra tabel header
headers = [header.text for header in data_tabel.find_all('th')]

# create a entry data set
df = pd.DataFrame(columns=headers)

rows = data_tabel.find_all('tr')
for table_row in rows[1:]:
    deta = table_row.find_all('td')
    row = [tr.text for tr in deta]
    lon = len(df)
    df.loc[lon] = row
print(df)

df.to_csv('stock_market_data.csv')



#Create by Nerov Ahmead








