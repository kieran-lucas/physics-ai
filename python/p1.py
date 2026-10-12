import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 200)
f = x**2
g = x**3
h = x**0.5
plt.plot(x, f, label = "f(x) = x²")
plt.plot(x, g, label = "g(x) = x³")
plt.plot(x, h, label = "h(x) = √x")
plt.title("Comparison of Three Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
