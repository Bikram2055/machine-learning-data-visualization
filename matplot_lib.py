import matplotlib.pyplot as plt
from numpy import random as r

# matplotlib.use('TkAgg')  in case of not showing plots

x = r.rand(10)
y = r.rand(10)
x2 = r.randint(5, size=10)
y2 = r.randint(5, size=10)

fig, ax = plt.subplots(2)
fig.suptitle('all graphs')

ax[0].hist(x, label='first')   # .boxplot()  plot()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
ax[1].scatter(x2, y2, label='second', linewidths=3, marker='x')
plt.title('scatter plot')
plt.legend()
plt.show()

# plt.subplot(1, 2, 1)
# plt.plot(x, y)
# plt.subplot(1, 2, 2)
# plt.plot(x2, y2)
# plt.show()