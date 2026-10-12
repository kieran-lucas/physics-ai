import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1, 11)
U = np.zeros((301, 11))
r = r = 0.1 * 0.001 / 0.1**2
U[0, :] = np.sin(np.pi * x)
for n in range(300):
    U[n+1, 1:-1] = U[n, 1:-1] + r * (
        U[n, 2:] - 2*U[n, 1:-1] + U[n, :-2]
    )
import matplotlib.pyplot as plt

plt.imshow(U, origin="lower", aspect="auto",
           extent=[0, 1, 0, 0.3])
plt.xlabel("x")
plt.ylabel("Time (s)")
plt.colorbar(label="Temperature")
plt.show()