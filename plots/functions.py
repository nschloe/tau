import numpy as np
import matplotlib.pyplot as plt
from math import tau
from scipy.special import erf, gamma, factorial, zeta
import matplotx

with plt.style.context(matplotx.styles.dracula):
    # cauchy
    x = np.linspace(-5.0, 5.0, 201)
    y = 1 / (1 + x**2)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\int_{-\infty}^{\infty} 1 / (1+x^2)$")
    # plt.gca().set_aspect('equal')
    plt.savefig("cauchy.svg")
    # plt.show()
    plt.close()

    # chebyshev
    x = np.linspace(-1.0, 1.0, 201)
    y = 1 / np.sqrt(1 - x**2)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\int_{-1}^1 1 / \sqrt{1-x^2}$")
    # plt.gca().set_aspect('equal')
    plt.savefig("chebyshev1.svg")
    # plt.show()
    plt.close()

    # chebyshev 2
    x = np.linspace(-1.0, 1.0, 201)
    y = np.sqrt(1 - x**2)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\int_{-1}^1 \sqrt{1-x^2}$")
    plt.gca().set_aspect("equal")
    plt.savefig("chebyshev2.svg")
    # plt.show()
    plt.close()

    # erf
    x = np.linspace(-5.0, 5.0, 201)
    y1 = erf(x)
    y2 = erf(x / np.sqrt(2))
    plt.plot(x, y1, label="$\mathrm{erf}$")
    plt.plot(x, y2, label="$\mathrm{erf}_1$")
    plt.legend()
    plt.savefig("erf.svg")
    plt.close()

    # gamma
    x = np.linspace(0.0, 6.0, 1001)
    y = gamma(x)
    # plt.semilogy(x, y)
    plt.plot(x, y)
    plt.title("$\Gamma(x)$")
    plt.xlabel("$x$")
    plt.ylim(0.0, 100.0)
    plt.savefig("gamma.svg")
    plt.close()

    # gaussian integral
    x = np.linspace(-5.0, 5.0, 201)
    y = np.exp(-(x**2))
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\int_{-\infty}^{\infty}\exp(-x^2)$")
    # plt.gca().set_aspect('equal')
    plt.savefig("gaussian.svg")
    # plt.show()
    plt.close()

    # laguerre
    x = np.linspace(0.0, 5.0, 201)
    plt.title(r"$\int_{-\infty}^{\infty}|x| \exp(-|x|)$")
    y = np.abs(x) * np.exp(-np.abs(x))
    plt.plot(x, y)
    plt.fill_between(x, y)
    # plt.gca().set_aspect('equal')
    plt.savefig("laguerre.svg")
    # plt.show()
    plt.close()

    nmax = 20
    x1 = np.arange(nmax + 1)
    y1 = [factorial(x) for x in x1]
    x2 = np.linspace(0, nmax, 300)
    y2 = np.sqrt(tau * x2) * (x2 / np.exp(1)) ** x2
    plt.semilogy(x1, y1, "o", label="n!", zorder=2)
    plt.semilogy(x2, y2, "-", label="Stirling", zorder=1)
    plt.xlabel("n")
    plt.legend()
    plt.savefig("stirling.svg")
    # plt.show()
    plt.close()

    # sinc
    x = np.linspace(-5.0, 5.0, 201)
    y = np.sinc(x)
    plt.plot(x, y, label="$sinc$")
    plt.plot(x, y**2, label="$sinc^2$")
    plt.plot(x, y**3, label="$sinc^3$")
    plt.legend()
    plt.savefig("sinc.svg")
    # plt.show()
    plt.close()

    # # zeta
    # x = np.linspace(0.0, 20.0, 1001)
    # y = zeta(x)
    # # plt.semilogy(x, y)
    # plt.plot(x, y)
    # plt.title("$\zeta(x)$")
    # plt.xlabel("$x$")
    # # plt.ylim(0.0, 100.0)
    # plt.savefig("zeta.svg")
    # # plt.show()
    # plt.close()
