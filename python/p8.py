import numpy as np
import matplotlib.pyplot as plt
y_pred = np.array([1, 3, 5, 7])
y_true = np.array([2, 2, 6, 8])
loss = np.mean((y_pred - y_true) ** 2)
max_loss = np.max((y_pred - y_true) ** 2)
max_loss_2 = np.max(np.abs(y_pred - y_true))
names = ["A", "B", "C", "D"]
values = np.abs(y_pred - y_true)
plt.bar(names, values)
plt.show()