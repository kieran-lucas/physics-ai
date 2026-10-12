import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)

y1 = x**2
y2 = 2*x

plt.plot(x, y1, label="y = x²")
plt.plot(x, y2, label="y = 2x")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()