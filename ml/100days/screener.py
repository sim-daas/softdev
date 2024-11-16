import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import time

# IMPORTANT DECLARATIONS

headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

col = ['Index', 'Name','CMP', 'PE', 'Market Cap', 'Dividend Yield', 'Net Profit Last Quarter', 'Quaterly Profit Growth', 'Sales Latest Quarter','Quaterly Sales Growth', 'Return on Campital Employment']
df = pd.DataFrame(columns=['Index', 'Name','CMP', 'PE', 'Market Cap', 'Dividend Yield', 'Net Profit Last Quarter', 'Quaterly Profit Growth', 'Sales Latest Quarter','Quaterly Sales Growth', 'Return on Campital Employment'])
x=0

# WEB SCRAPING

for i in range(1, 88):
    print(i)
    if i < 10:
        url=f"https://www.screener.in/company/compare/0000000{i}/?page=1"
    else:
        url=f"https://www.screener.in/company/compare/000000{i}/?page=1"

    page = requests.get(url, headers=headers)
    page = page.text
    page = bs(page, 'html.parser')

    if [div for div in page.find_all('div', class_="sub") if 'font-size-13' not in div.get('class', [])]:
        filtered_divs = [div for div in page.find_all('div', class_="sub") if 'font-size-13' not in div.get('class', [])]
        nump=int(filtered_divs[0].text.split()[-1])
    else:
        filtered_divs = page.find_all('div', class_="sub")
        nump=1

    for j in range(1, nump+1):
        if i < 10:
            url=f"https://www.screener.in/company/compare/0000000{i}/?page={j}"
        else:
            url=f"https://www.screener.in/company/compare/000000{i}/?page={j}"

        page = requests.get(url, headers=headers)
        page = page.text
        page = bs(page, 'html.parser')
        data = []
        
        for r in range(0, len(page.find_all('tr'))):
            data.append(page.find_all('tr')[r].find_all('td'))

        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                df.loc[i+x, col[j]] = data[i][j].text
        x = len(df)
        
    time.sleep(5)
    

# CLEANING

df.drop(columns=['Index'], inplace=True)
df['Name'] = df['Name'].replace('\n', '', regex=True) 
df.drop_duplicates(subset=['Name'], keep='first', inplace=True) 
df.shape 

df = pd.read_csv('./dataset/screener.csv')
df.head()

df.isna().sum()

for i in range(2, len(col)):
    df.loc[df[col[i]].isna(), col[i]] = df[col[i]].mean()
    
df.to_csv('./dataset/screener.csv', index=False) 