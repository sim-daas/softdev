# Data exploration

import opendatasets as opd
import pandas as pd
import numpy as np

opd.download("https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot/")
opd.download("https://www.kaggle.com/datasets/dansbecker/home-data-for-ml-course")
mlbd = pd.read_csv("melbourne-housing-snapshot/melb_data.csv")
mlbd.head()

home_data = pd.read_csv("home-data-for-ml-course/train.csv")
home_data.head()

home_data.describe()
avg_lot_size = home_data.describe().loc["mean", "LotArea"]
newest_home_age = (2024 - home_data.describe().loc["max", "YearBuilt"])




# Training Basic model on melbourne house dataset

# Data cleaning

mlbd.columns
mlbd = mlbd.dropna()
mlbd.head()

y = mlbd.Price
y

x = mlbd.loc[:, ["Rooms", "Bathroom", "Landsize", "Lattitude", "Longtitude"]]
x


# Model Training

from sklearn.tree import DecisionTreeRegressor

mbmodel = DecisionTreeRegressor(random_state=1)

mbmodel.fit(x, y)



# Model prediction 

print(mlbd.head()["Price"])
mbmodel.predict(x.head())




# Model training exercise

home_data.head()
home_data.describe()
home_data.columns
home_data.sample(5)

y = home_data.SalePrice
x = home_data[["LotArea", "LotFrontage", "PoolArea","YrSold"]]


hmmodel = DecisionTreeRegressor(random_state=1)
hmmodel.fit(x, y)

print(home_data.head().SalePrice)
hmmodel.predict(x.head())




















