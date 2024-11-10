import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url="https://hurawatch.cc/search/marvel"
page = requests.get(url, headers=headers)
page = page.text
page = bs(page, 'html.parser')

add = page.find_all('div', class_='film-poster')[0].find('a')['href']
flmurl = "https://hurawatch.cc" + add
flmpage = requests.get(flmurl, headers=headers)
flmpage = flmpage.text
flmpage = bs(flmpage, 'html.parser')

page.find_all('div', class_='film-detail')[0]
print("duration ", page.find_all('div', class_='film-detail')[0].find('span', class_='fdi-item fdi-duration').text.split())


for i in range(0, len(page.find_all('div', class_='film-detail'))):
    if page.find_all('div', class_='film-detail')[i].find("span", class_='float-right fdi-type').text.split() == ['Movie']:
        print("movie name ", page.find_all('div', class_='film-detail')[i].find('h2').text.strip())
        print("duration ", page.find_all('div', class_='film-detail')[i].find('span', class_='fdi-item fdi-duration').text.split()[0])
        add = page.find_all('div', class_='film-poster')[i].find('a')['href']
        flmurl = "https://hurawatch.cc" + add
        flmpage = requests.get(flmurl, headers=headers)
        flmpage = flmpage.text
        flmpage = bs(flmpage, 'html.parser')
        print(flmpage.find_all('span', class_='item mr-3')[1].text.split())
    elif page.find_all('div', class_='film-detail')[i].find('span', class_='float-right fdi-type').text.split() == ['TV']:
        print("series name ", page.find_all('div', class_='film-detail')[i].find('h2').text.strip())
        print("season ", page.find_all('div', class_='film-detail')[i].find('span', class_= "fdi-item").text.strip())
        add = page.find_all('div', class_='film-poster')[i].find('a')['href']
        flmurl = "https://hurawatch.cc" + add
        flmpage = requests.get(flmurl, headers=headers)
        flmpage = flmpage.text
        flmpage = bs(flmpage, 'html.parser')
        print(flmpage.find_all('span', class_='item mr-3')[1].text.split())
    else:
        pass
    print('\n')


add = page.find_all('div', class_='film-poster')[0].find('a')['href']
flmurl = "https://hurawatch.cc" + add
flmpage = requests.get(flmurl, headers=headers)
flmpage = flmpage.text
flmpage = bs(flmpage, 'html.parser')

flmpage.find_all('span', class_='item mr-3')[1].text.split()
























 