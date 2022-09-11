import sklearn.datasets as ds
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, mean_squared_error
from matplotlib import pyplot as plt

iris = ds.load_iris()
data1 = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                     columns=iris['feature_names'] + ['target'])
print(data1.head())

understanding data
print(data1.describe())
print(data1.columns)
print(data1.shape)
print(data1.isnull().sum())
print(data1.info())
print(data1['target'].unique().sum())
data2 = data1.drop(columns='target')

scale = MinMaxScaler()
data2 = scale.fit_transform(data2)  # preprocessing
# print(data2)

# attributes = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
#               'petal width (cm)']
# scatter_matrix(data1[attributes])  # strong correlation between features (feature selection)
# plt.show()

train_x, test_x, train_y, test_y = train_test_split(data2, data1['target'], train_size=0.80, test_size=0.20)
# print(test_y)

# distorsion = []
# for k in range(2, 10):
#     kmean = KMeans(n_clusters=k)
#     kmean.fit(train_x)
#     distorsion.append(kmean.inertia_)

# fig = plt.figure(figsize=(15, 5))
# plt.plot(range(2, 20), distorsions)
# plt.grid(True)
# plt.title('Elbow curve')
# plt.show()
# kmean = KMeans(n_clusters=3)
# kmean.fit(train_x)
#
# test = kmean.predict(test_x)
# print(f'result:- {test}')
# print(f'expected:- {test_y}')


# kmeans = KMeans(n_clusters=3)
# kmeans.fit(train_x, train_y)
# # training predictions
# train_labels = kmeans.predict(train_x)
#
# # testing predictions
# test_labels = kmeans.predict(test_x)
# # training accuracy
# print(accuracy_score(train_y, train_labels) * 100)
# # testing accuracy
# print(accuracy_score(test_labels, test_y) * 100)

kmean = KMeans(n_clusters=3)
kmean.fit(train_x)
prediction = kmean.predict(test_x)
acc = accuracy_score(test_y, prediction)
mean = mean_squared_error(test_y, prediction)
print('accuracy:- ', acc*100)
print('mean square error:- ', mean)
