import pandas as pd
import numpy as np


df = pd.DataFrame([[1,2,3],[4,5,6]])
df.head()

results = pd.read_parquet('./data/results.parquet')     
bios = pd.read_csv('./data/bios.csv') 
results.columns

df = pd.read_csv('./data/coffee.csv')
df.head()

df.columns
df.index

df['Day'][2]
df.sample(5)

df.head()
df.loc[[0,1,3]]
df.loc[0:3]
df.loc[0:3, "Day"]
df.loc[2, ["Day", "Coffee Type"]]
df.iloc[0:2, [0,1,2]] #only indexes can be used

df.head()
df.iloc[0,1] = "Latte"
df.loc[0,"Coffee Type"]


df.head()
df.sort_values("Units Sold", ascending=0)
df.sort_values(["Units Sold", "Coffee Type"], ascending=[0,1])

bios.columns
bios.head()
bios.sample(5)
bios[bios.height_cm == 183.0]
bios.loc[bios.height_cm == 183.0, "height_cm"]
bios[bios["height_cm"] == 183.0]["name"]
bios.loc[bios["height_cm"] == 183.0, ["name", "height_cm"]]
bios.loc[(bios["height_cm"] == 183.0) & (bios.born_country == "IND"), ["name", "height_cm"]]
bios.loc[bios.name.str.contains("Keith")]
bios.loc[bios.name.str.contains("Keith") & (bios.height_cm >= 180.0)]
bios.query('born_country == "USA" and height_cm == 180.0')


df.head()
df.loc[0] = "Tuesday", "asasa",30
df.head()


import opendatasets as opd

opd.download("https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot/")
opd.download("https://www.kaggle.com/datasets/dansbecker/home-data-for-ml-course")
new = pd.read_csv("melbourne-housing-snapshot/melb_data.csv")
new.head()

home_data = pd.read_csv("home-data-for-ml-course/train.csv")
home_data.head()






