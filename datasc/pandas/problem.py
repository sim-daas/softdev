import pandas as pd

print(pd.__version__)

print(pd.show_versions()) 

import numpy as np


data = {
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, labels)

# 5
df.info()

# 6
df.head(3)

# 7
df[["animal", 'age']]

# 8
df.iloc[[3,4,8], 0:2]

# 9
df[df['visits'] > 3]

# 10





