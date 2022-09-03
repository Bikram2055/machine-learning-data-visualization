import sklearn.datasets as ds
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, r2_score
from matplotlib import pyplot as plt

iris = ds.load_iris()
ds.load_diabetes()
data1 = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                     columns=iris['feature_names'] + ['target'])

data2 = data1.drop(columns='target')

scale = MinMaxScaler()  # pre-processing
data2 = scale.fit_transform(data2)
# print(data2)

# feature selection ::- in this data sets all 4 feature are

train_x, test_x, train_y, test_y = train_test_split(data2, data1['target'], train_size=0.80, test_size=0.20)

# for diabetes dataset of sklearn use linear regression model
# model = LinearRegression().fit(train_x, train_y)
# test = model.predict(test_x)
# acc = r2_score(test, test_y)
# print(acc*100)
# plt.plot(test)
# list_test_y = test_y.tolist()
# data = np.array(list_test_y)
# plt.plot(data)
# plt.show()


model = KNeighborsClassifier(n_neighbors=3)
# model = SVC()
# model = LogisticRegression()

model.fit(train_x, train_y)
test = model.predict(test_x)
acc = accuracy_score(test, test_y)
print(acc * 100)

# print(model.predict([[4.9, 3.0, 1.4, 0.2]]))
# plt.plot(test)
# list_test_y = test_y.tolist()
# data = np.array(list_test_y)
# plt.plot(data)
# plt.show()

# naive bais

# X, y = ds.load_iris(return_X_y=True)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
# gnb = GaussianNB()
# y_pred = gnb.fit(X_train, y_train).predict(X_test)
# print("Number of mislabeled points out of a total %d points : %d"
#       % (X_test.shape[0], (y_test != y_pred).sum()))
