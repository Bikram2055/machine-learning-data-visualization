import pandas as pd
import numpy as np

a = np.random.rand(100)
x = a.reshape(25, 4)
df = pd.DataFrame(x)
# print(df)
# print('\n---head---\n')
# print(df.head())  # there is tail() function also
# print(df.describe())  # return analytical data about dataframe
#
# c = df.to_numpy()
# print(c)
shit = pd.read_csv('C:/Users/ACER/OneDrive/Documents/report card')
print(shit)