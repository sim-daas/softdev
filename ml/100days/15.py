import pandas as pd
import numpy as np

def yearch(year):
    return int(year) - 2000

df = pd.read_csv("~/githubrepos/softdev/datasc/pandas/home-data-for-ml-course/train.csv", index_col=["Id"], converters={'YrSold':yearch})
df.drop(columns=['Alley', 'PoolQC', 'MiscFeature'], inplace=True)
df.sample(10)


# creating a hot encoder on column 'MSZoning'

df = pd.get_dummies(df, columns=['MSZoning'], drop_first=True)
df.sample(10)










































