import numpy as np
y_pred = np.array([2, 4, 7])
y_true = np.array([3, 5, 6])
loss = np.mean((y_pred - y_true) ** 2)
print(loss)