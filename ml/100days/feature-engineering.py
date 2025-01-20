import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import MinMaxScaler


# 1. Standardization

df = pd.read_csv('data/ads.csv')
df = df.iloc[:, 2:]
df.head()

scaler = StandardScaler()

scaler.fit(df)

df_scaled = scaler.transform(df)

df_scaled = pd.DataFrame(df_scaled, columns=df.columns)

df_scaled.head()






















