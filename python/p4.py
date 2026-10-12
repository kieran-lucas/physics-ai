import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 200)
f = x**2
g = x**3
h = x**0.5
plt.plot(x, f, label = "f(x) = x²", color = 'blue', linewidth = 2, linestyle = "-")
plt.plot(x, g, label = "g(x) = x³", color = 'red', linewidth = 1.5, linestyle = "--")
plt.plot(x, h, label = "h(x) = √x", color = 'green', linewidth = 3, linestyle = ":")
plt.title("Comparison of Three Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("graph.pdf")
plt.show()
