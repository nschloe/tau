import numpy as np
from math import factorial, tau
import matplotlib.pyplot as plt

nmax = 20
x1 = np.arange(nmax + 1)
y1 = [factorial(x) for x in x1]

x2 = np.linspace(0, nmax, 300)
y2 = np.sqrt(tau * x2) * (x2/np.exp(1))**x2

plt.semilogy(x1, y1, "o", label="n!", zorder=2)
plt.semilogy(x2, y2, "-", label="Stirling", zorder=1)
plt.xlabel("n")
plt.legend()
plt.show()
