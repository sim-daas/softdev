import numpy as np
import pandas as pd

df = pd.read_csv('./data/train.csv')
df.head()
df.info()
df.isnull().sum()

df.loc[df.Age.isna(), 'Age'] = df.Age.mean()
df.isnull().sum()
df.drop(columns=)












