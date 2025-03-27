import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('./house.csv')
df.sample(5)
df.columns

df.info()
df.describe()

sns.distplot(df['total_bedrooms'])
sns.boxplot(df["population"])
sns.boxplot(df["total_bedrooms"])


df.loc[df.total_bedrooms.isna()] = df.total_bedrooms.mean()
df.isnull().sum()

# Remove outliers using IQR on 'population' column
Q1 = df['population'].quantile(0.25)
Q3 = df['population'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['population'] >= Q1 - 1.5 * IQR) & (df['population'] <= Q3 + 1.5 * IQR)]

# Remove outliers using IQR on 'total_bedrooms' column
Q1 = df['total_bedrooms'].quantile(0.25)
Q3 = df['total_bedrooms'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['total_bedrooms'] >= Q1 - 1.5 * IQR) & (df['total_bedrooms'] <= Q3 + 1.5 * IQR)]

scaler = StandardScaler()
df['total_bedrooms'] = scaler.fit_transform(df[['total_bedrooms']])








