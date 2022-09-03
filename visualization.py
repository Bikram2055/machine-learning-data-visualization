import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

# print(data.head())
# print(data.tail())

# print(data.isnull().sum())

# print(data.columns)
data = data.drop(columns='Unnamed: 2')
# print(data.columns)

# print(data.head())

# print(data.describe())
# print('*'*100)
# print(data.info())

# print(data.isnull().sum())
data.dropna(how='all', inplace=True)  # drop all rows having all null values, inplace change dataframe
# print(data.isnull().sum())

# a = data.loc[data['PARTICULAR'] == 'magic vada']  # select rows with one specific value of one column
# print(a['AMOUNT'].sum())

unique = data['PARTICULAR'].unique()
print(unique)

e = list(data['PARTICULAR'].unique())
# print("no. of unique items:- ", len(e))
lis = []
for i in e:
    a = data.loc[data['PARTICULAR'] == i]
    b = a['AMOUNT'].sum()
    lis.append(b)
    print(f'for {i} total expends(rs):- ', b)

# plt.pie(lis, labels=unique)
# plt.legend()
# plt.show()

# plt.hist(lis)
# plt.show()

# plt.bar(unique, lis)
# plt.xlabel('field-->')
# plt.ylabel('expenses-->')
# plt.show()
