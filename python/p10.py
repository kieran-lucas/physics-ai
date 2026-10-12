import numpy as np
A = np.array([[1, 1], [1, 2], [1, 3]])
b = np.array([2, 3, 5])
print(A.shape)
print(b.shape)
w = np.linalg.lstsq(A, b, rcond = None)[0]
y_pred = A @ w
loss = np.mean((y_pred - b) ** 2)

print(w)
