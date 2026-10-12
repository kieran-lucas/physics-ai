import numpy as np
import matplotlib.pyplot as plt

w = 0.0
lr = 0.1
loss_history = []
for i in range(100):
    gradient = 2 * (w - 2)
    w -= lr * gradient
    loss_history.append((w - 2) ** 2)
    print(w)

plt.title("Gradient Descent Convergence")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.plot(loss_history, color='blue', linewidth=2)
plt.grid(True)
plt.show()

