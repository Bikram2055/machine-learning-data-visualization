import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('gold.csv')

# data = pd.to_datetime(data['Date'])
# print(data['price'])

x = [i for i in range(len(data['price']))]
y = []
for i in range(len(data['price'])):
    list1 = data['price'][i].split(',')
    a = ''.join(list1)
    y.append(int(a)/1000)

plt.plot(x, y)
plt.show()
