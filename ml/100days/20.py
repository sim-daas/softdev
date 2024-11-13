import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./data/train.csv', index_col=0)
df.sample(5)

df.info()

df['Survived'].value_counts().plot(kind='bar')
plt.show()

# Count Plot (Bar Plot)

sns.countplot(data=df, x='Survived')
plt.show()

sns.countplot(data=df, x='Sex')
plt.show()

sns.countplot(data=df, x='Pclass', hue='Survived')
plt.show()

sns.countplot(data=df, x='Sex', hue='Survived')
plt.show()

sns.countplot(data=df, x='Pclass', hue='Sex')
plt.show()

# Bar Plot

sns.barplot(data=df, x='Sex' ,y='Age')
plt.show()

sns.barplot(data=df, x='Pclass', y='Age', hue='Sex')
plt.show()

# Histogram

sns.histplot(data=df, x="Age", bins=50)
plt.show()











