import numpy as np

x = np.linspace(0, 4, 101)
y = x**3

dy = np.gradient(y, x)
print(dy[50])