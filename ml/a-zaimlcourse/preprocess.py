import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')
df.info()

df.head()

x = df.iloc[:, 0:3]
x.info()
x.head()

y = df.iloc[:, 3]
y.info()
y.head()

df.isna()













