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
    y1 = np.exp(-(x**2))
    plt.plot(x, y1, label="$\exp(-x^2)$")
    plt.fill_between(x, y1, zorder=2)
    y2 = np.exp(-(x**2/2))
    plt.plot(x, y1, label="$\exp(-x^2/2)$")
    plt.fill_between(x, y2, zorder=1)
    # plt.title(r"$\int_{-\infty}^{\infty}\exp(-x^2/2)$")
    # plt.gca().set_aspect('equal')
    plt.legend()
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
    # plt.plot(x, y, label="$sinc$")
    plt.fill_between(x, y, zorder=1, label="$sinc$")
    # plt.plot(x, y**2, label="$sinc^2$")
    plt.fill_between(x, y**2, zorder=2, label="$sinc^2$")
    # plt.plot(x, y**3, label="$sinc^3$")
    plt.fill_between(x, y**3, zorder=3, label="$sinc^3$")
    plt.legend()
    plt.savefig("sinc.svg")
    # plt.show()
    plt.close()

    # borwein
    x = np.linspace(-5.0, 5.0, 201)
    y = np.sinc(x)
    # plt.plot(x, y, label="$sinc(x)$")
    plt.fill_between(x, y, zorder=1, label="$sinc(x)$")
    y *= np.sinc(x/3)
    # plt.plot(x, y, label="$sinc(x) sinc(x/3)$")
    plt.fill_between(x, y, zorder=1, label="$sinc(x) sinc(x/3)$")
    y *= np.sinc(x/5)
    # plt.plot(x, y, label="$sinc(x) sinc(x/3) sinc(x/5)$")
    plt.fill_between(x, y, zorder=1,label="$sinc(x) sinc(x/3) sinc(x/5)$")
    plt.legend()
    plt.savefig("borwein.svg")
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

    # wigner semicircle
    x = np.linspace(-2.0, 2.0, 201)
    y = np.sqrt(4.0 - x**2) / tau
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\sqrt{4 - x^2} / \tau$")
    plt.savefig("semicircle.svg")
    plt.close()

    # chord / Euler reflection formula
    z = 0.3
    theta = tau * z
    fig, ax = plt.subplots(figsize=(5, 5))
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    c0, c1, c2 = colors[0], colors[1], colors[2]

    t = np.linspace(0, tau, 400)
    ax.plot(np.cos(t), np.sin(t), color="gray", lw=1, alpha=0.6)

    A = np.array([1.0, 0.0])
    B = np.array([np.cos(theta), np.sin(theta)])

    # arc tau*z
    ta = np.linspace(0, theta, 100)
    ax.plot(1.08 * np.cos(ta), 1.08 * np.sin(ta), color=c1, lw=2)
    ax.text(1.2 * np.cos(theta / 2), 1.2 * np.sin(theta / 2),
            r"$\tau z$", color=c1, ha="center", va="center", fontsize=14)
    # complementary arc tau*(1-z)
    tb = np.linspace(theta, tau, 200)
    ax.plot(1.08 * np.cos(tb), 1.08 * np.sin(tb), color=c1, lw=2, alpha=0.35)
    ax.text(1.22 * np.cos((theta + tau) / 2), 1.22 * np.sin((theta + tau) / 2),
            r"$\tau (1-z)$", color=c1, alpha=0.6, ha="center", va="center", fontsize=14)

    # radii
    ax.plot([0, A[0]], [0, A[1]], color="gray", lw=1, ls="--")
    ax.plot([0, B[0]], [0, B[1]], color="gray", lw=1, ls="--")
    # half-angle bisector to chord midpoint
    M = (A + B) / 2
    ax.plot([0, M[0]], [0, M[1]], color="gray", lw=1, ls=":")
    th = np.linspace(0, theta / 2, 50)
    ax.plot(0.25 * np.cos(th), 0.25 * np.sin(th), color="gray", lw=1)
    ax.text(0.36 * np.cos(theta / 4), 0.36 * np.sin(theta / 4),
            r"$\tau z/2$", color="gray", ha="center", va="center", fontsize=11)

    # chord
    ax.plot([A[0], B[0]], [A[1], B[1]], color=c0, lw=3)
    n = np.array([-(B - A)[1], (B - A)[0]])
    n /= np.linalg.norm(n)
    L = M - 0.16 * n
    ax.text(L[0], L[1], r"$\mathrm{crd}(\tau z) = 2\sin(\tau z/2)$",
            color=c0, ha="center", va="center", fontsize=12,
            rotation=(np.degrees(np.arctan2(*(B - A)[::-1])) + 90) % 180 - 90)

    ax.plot(*A, "o", color=c2)
    ax.plot(*B, "o", color=c2)
    ax.text(A[0] + 0.06, A[1] - 0.1, r"$1$", color=c2, fontsize=13)
    ax.text(B[0] - 0.08, B[1] + 0.08, r"$e^{i\tau z}$", color=c2, fontsize=13,
            ha="right")

    ax.set_aspect("equal")
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.axis("off")
    ax.set_title(r"$\Gamma(z)\,\Gamma(1-z) = \tau \,/\, \mathrm{crd}(\tau z)$", fontsize=14)
    fig.savefig("chord.svg", bbox_inches="tight")
    plt.close()
