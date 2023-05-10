import numpy as np
import matplotlib.pyplot as plt
import matplotx

x = np.linspace(-5.0, 5.0, 201)

y = np.sinc(x)

with plt.style.context(matplotx.styles.dracula):
    plt.plot(x, y,    label="$sinc$")
    plt.plot(x, y**2, label="$sinc^2$")
    plt.plot(x, y**3, label="$sinc^3$")
    plt.legend()

# plt.savefig("cauchy.svg")
plt.show()
