import numpy as np
import matplotlib.pyplot as plt
from math import tau
from scipy.special import erf, gamma, factorial, zeta
import matplotx
from cycler import cycler

# Two variants of every plot: the Dracula style for dark mode, and a light
# counterpart with the same color roles (c0 blue/cyan, c1 orange, c2 green,
# c3 red, ...) on white. The README picks one via <picture>.
dark = dict(matplotx.styles.dracula)
light = {
    **dark,
    "lines.color": "#282a36",
    "patch.edgecolor": "#282a36",
    "text.color": "#282a36",
    "axes.facecolor": "white",
    "axes.edgecolor": "#282a36",
    "axes.labelcolor": "#282a36",
    "xtick.color": "#282a36",
    "ytick.color": "#282a36",
    "grid.color": "#cccccc",
    "figure.facecolor": "white",
    "figure.edgecolor": "white",
    "savefig.facecolor": "white",
    "savefig.edgecolor": "white",
    "axes.prop_cycle": cycler(
        "color",
        ["#1f77b4", "#e8710a", "#2ca02c", "#d62728", "#9467bd", "#e377c2", "#7f7f7f", "#bcbd22"],
    ),
}

for style, suffix in [(dark, ""), (light, "-light")]:
  with plt.style.context(style):
    # foreground color for annotations that were hard-coded white
    fg = plt.rcParams["text.color"]
    # cauchy
    x = np.linspace(-5.0, 5.0, 201)
    y = 1 / (1 + x**2)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\int_{-\infty}^{\infty} 1 / (1+x^2)$")
    # plt.gca().set_aspect('equal')
    plt.savefig(f"cauchy{suffix}.svg")
    # plt.show()
    plt.close()

    # chebyshev
    x = np.linspace(-1.0, 1.0, 201)
    y = 1 / np.sqrt(1 - x**2)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\int_{-1}^1 1 / \sqrt{1-x^2}$")
    # plt.gca().set_aspect('equal')
    plt.savefig(f"chebyshev1{suffix}.svg")
    # plt.show()
    plt.close()

    # chebyshev 2
    x = np.linspace(-1.0, 1.0, 201)
    y = np.sqrt(1 - x**2)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\int_{-1}^1 \sqrt{1-x^2}$")
    plt.gca().set_aspect("equal")
    plt.savefig(f"chebyshev2{suffix}.svg")
    # plt.show()
    plt.close()

    # erf
    x = np.linspace(-5.0, 5.0, 201)
    y1 = erf(x)
    y2 = erf(x / np.sqrt(2))
    plt.plot(x, y1, label="$\mathrm{erf}$")
    plt.plot(x, y2, label="$\mathrm{erf}_1$")
    plt.legend()
    plt.savefig(f"erf{suffix}.svg")
    plt.close()

    # gamma
    x = np.linspace(0.0, 6.0, 1001)
    y = gamma(x)
    # plt.semilogy(x, y)
    plt.plot(x, y)
    plt.title("$\Gamma(x)$")
    plt.xlabel("$x$")
    plt.ylim(0.0, 100.0)
    plt.savefig(f"gamma{suffix}.svg")
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
    plt.savefig(f"gaussian{suffix}.svg")
    # plt.show()
    plt.close()

    # laguerre
    x = np.linspace(0.0, 5.0, 201)
    plt.title(r"$\int_{-\infty}^{\infty}|x| \exp(-|x|)$")
    y = np.abs(x) * np.exp(-np.abs(x))
    plt.plot(x, y)
    plt.fill_between(x, y)
    # plt.gca().set_aspect('equal')
    plt.savefig(f"laguerre{suffix}.svg")
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
    plt.savefig(f"stirling{suffix}.svg")
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
    plt.savefig(f"sinc{suffix}.svg")
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
    plt.savefig(f"borwein{suffix}.svg")
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
    # plt.savefig(f"zeta{suffix}.svg")
    # # plt.show()
    # plt.close()

    # wigner semicircle
    x = np.linspace(-2.0, 2.0, 201)
    y = np.sqrt(4.0 - x**2) / tau
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.title(r"$\sqrt{4 - x^2} / \tau$")
    plt.savefig(f"semicircle{suffix}.svg")
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
    fig.savefig(f"chord{suffix}.svg", bbox_inches="tight")
    plt.close()

    # ---------------------------------------------------------------------
    # Euler's identity: exp(i tau t), t from 0 to 1, is one full turn
    fig, ax = plt.subplots(figsize=(5, 5))
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    c0, c1, c2 = colors[0], colors[1], colors[2]
    t = np.linspace(0, tau, 400)
    ax.plot(np.cos(t), np.sin(t), color=c1, lw=2.5)
    for k in range(4):
        a = (k + 0.5) * tau / 4
        ax.annotate(
            "",
            xy=(np.cos(a + 0.02), np.sin(a + 0.02)),
            xytext=(np.cos(a), np.sin(a)),
            arrowprops=dict(arrowstyle="-|>", color=c1, lw=2, mutation_scale=22),
        )
    labels = [
        r"$t=1$: $e^{i\tau} = 1$",
        r"$t=\frac{1}{4}$: $e^{i\tau/4} = i$",
        r"$t=\frac{1}{2}$: $e^{i\tau/2} = -1$",
        r"$t=\frac{3}{4}$: $e^{i3\tau/4} = -i$",
    ]
    offsets = [(1.08, -0.12, "left"), (0.0, 1.12, "center"), (-1.08, -0.12, "right"), (0.0, -1.2, "center")]
    for k, (lab, (dx, dy, ha)) in enumerate(zip(labels, offsets)):
        a = k * tau / 4
        ax.plot([0, np.cos(a)], [0, np.sin(a)], color="gray", lw=1, ls="--")
        ax.plot(np.cos(a), np.sin(a), "o", color=c2, ms=8)
        ax.text(dx, dy, lab, color=c2, ha=ha, va="center", fontsize=12)
    ax.text(0, 0.1, r"$t=0$ and $t=1$" "\n" "are the same point", color="gray",
            ha="center", va="bottom", fontsize=10)
    ax.set_aspect("equal")
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.5, 1.5)
    ax.axis("off")
    ax.set_title(r"$t \mapsto e^{i\tau t}$: one full turn", fontsize=14)
    fig.savefig(f"euler_identity{suffix}.svg", bbox_inches="tight")
    plt.close()

    # ---------------------------------------------------------------------
    # nth roots of unity
    n = 7
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(np.cos(t), np.sin(t), color="gray", lw=1, alpha=0.6)
    k = np.arange(n)
    zs = np.exp(1j * tau * k / n)
    ax.plot(np.append(zs.real, zs[0].real), np.append(zs.imag, zs[0].imag),
            color=c0, lw=1.5, alpha=0.7)
    ax.plot([0, zs[0].real], [0, zs[0].imag], color="gray", lw=1, ls="--")
    ax.plot([0, zs[1].real], [0, zs[1].imag], color="gray", lw=1, ls="--")
    th = np.linspace(0, tau / n, 50)
    ax.plot(0.35 * np.cos(th), 0.35 * np.sin(th), color=c1, lw=2)
    ax.text(0.55 * np.cos(tau / n / 2), 0.55 * np.sin(tau / n / 2), r"$\tau/7$",
            color=c1, ha="center", va="center", fontsize=13)
    ax.plot(zs.real, zs.imag, "o", color=c2, ms=9)
    for kk, z in zip(k, zs):
        ax.text(1.22 * z.real, 1.22 * z.imag, rf"$e^{{i\tau\cdot {kk}/7}}$",
                color=c2, ha="center", va="center", fontsize=11)
    ax.set_aspect("equal")
    ax.set_xlim(-1.55, 1.55)
    ax.set_ylim(-1.45, 1.45)
    ax.axis("off")
    ax.set_title(r"$z^7 = 1$", fontsize=14)
    fig.savefig(f"roots{suffix}.svg", bbox_inches="tight")
    plt.close()

    # ---------------------------------------------------------------------
    # circle as a triangle: A = 1/2 * tau r * r
    from matplotlib.patches import Polygon, Wedge

    N = 10
    r = 1.0
    cmap = plt.get_cmap("viridis")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.2), gridspec_kw={"width_ratios": [1, 2.6]})
    for kk in range(N):
        rho_out = (kk + 1) * r / N
        ax1.add_patch(Wedge((0, 0), rho_out, 0, 360, width=r / N,
                            facecolor=cmap(kk / (N - 1)), edgecolor="none"))
        # strip at distance rho from apex has width tau*rho; base at bottom
        rho0, rho1 = kk * r / N, rho_out
        ax2.add_patch(Polygon(
            [(-tau * rho0 / 2, r - rho0), (tau * rho0 / 2, r - rho0),
             (tau * rho1 / 2, r - rho1), (-tau * rho1 / 2, r - rho1)],
            closed=True, facecolor=cmap(kk / (N - 1)), edgecolor="none"))
    ax1.plot([0, r], [0, 0], color=fg, lw=1)
    ax1.text(r / 2, 0.08, r"$r$", color=fg, ha="center", fontsize=13)
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax2.annotate("", xy=(tau / 2, -0.12), xytext=(-tau / 2, -0.12),
                 arrowprops=dict(arrowstyle="<->", color=fg, lw=1))
    ax2.text(0, -0.3, r"$\tau r$", color=fg, ha="center", fontsize=13)
    ax2.annotate("", xy=(tau / 2 + 0.15, r), xytext=(tau / 2 + 0.15, 0),
                 arrowprops=dict(arrowstyle="<->", color=fg, lw=1))
    ax2.text(tau / 2 + 0.3, r / 2, r"$r$", color=fg, va="center", fontsize=13)
    ax2.set_xlim(-tau / 2 - 0.2, tau / 2 + 0.6)
    ax2.set_ylim(-0.45, 1.1)
    ax2.set_aspect("equal")
    ax2.axis("off")
    fig.suptitle(r"$A = \frac{1}{2}\cdot \tau r \cdot r = \frac{1}{2}\tau r^2$", fontsize=14)
    fig.savefig(f"sector{suffix}.svg", bbox_inches="tight")
    plt.close()

    # ---------------------------------------------------------------------
    # exterior angles of a polygon sum to tau
    V = np.array([(0.0, 0.0), (3.0, 0.3), (3.8, 2.2), (1.8, 3.4), (-0.6, 2.0)])
    m = len(V)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw={"width_ratios": [1.3, 1]})
    ax1.add_patch(Polygon(V, closed=True, facecolor="none", edgecolor=fg, lw=2))
    angles = []
    for i in range(m):
        d_in = V[i] - V[i - 1]
        d_out = V[(i + 1) % m] - V[i]
        a_in = np.degrees(np.arctan2(d_in[1], d_in[0]))
        a_out = np.degrees(np.arctan2(d_out[1], d_out[0]))
        ext = (a_out - a_in) % 360
        angles.append((a_in, ext))
        e = d_in / np.linalg.norm(d_in)
        ax1.plot([V[i, 0], V[i, 0] + 1.1 * e[0]], [V[i, 1], V[i, 1] + 1.1 * e[1]],
                 color="gray", lw=1, ls="--")
        ax1.add_patch(Wedge(V[i], 0.7, a_in, a_in + ext, facecolor=colors[i % len(colors)],
                            alpha=0.8, edgecolor="none"))
    start = 0.0
    for i, (a_in, ext) in enumerate(angles):
        ax2.add_patch(Wedge((0, 0), 1.0, start, start + ext, facecolor=colors[i % len(colors)],
                            alpha=0.8, edgecolor="none"))
        start += ext
    ax1.set_xlim(-1.6, 5.0)
    ax1.set_ylim(-1.2, 4.6)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("exterior angles", fontsize=13)
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-1.2, 1.2)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title(r"$\sum_k \varepsilon_k = \tau$", fontsize=13)
    fig.savefig(f"exterior{suffix}.svg", bbox_inches="tight")
    plt.close()

    # ---------------------------------------------------------------------
    # turning tangents (Hopf's Umlaufsatz)
    s = np.linspace(0, tau, 400)
    a_, b_, phi = 1.5, 1.0, np.radians(25)
    X = a_ * np.cos(s) * np.cos(phi) - b_ * np.sin(s) * np.sin(phi)
    Y = a_ * np.cos(s) * np.sin(phi) + b_ * np.sin(s) * np.cos(phi)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.8), gridspec_kw={"width_ratios": [1.5, 1]})
    ax1.plot(X, Y, color="gray", lw=1.5)
    hsv = plt.get_cmap("hsv")
    narr = 12
    for i, si in enumerate(np.linspace(0, tau, narr, endpoint=False)):
        p = np.array([a_ * np.cos(si) * np.cos(phi) - b_ * np.sin(si) * np.sin(phi),
                      a_ * np.cos(si) * np.sin(phi) + b_ * np.sin(si) * np.cos(phi)])
        d = np.array([-a_ * np.sin(si) * np.cos(phi) - b_ * np.cos(si) * np.sin(phi),
                      -a_ * np.sin(si) * np.sin(phi) + b_ * np.cos(si) * np.cos(phi)])
        d /= np.linalg.norm(d)
        col = hsv(i / narr)
        ax1.annotate("", xy=p + 0.5 * d, xytext=p,
                     arrowprops=dict(arrowstyle="-|>", color=col, lw=2, mutation_scale=16))
        ax2.annotate("", xy=d, xytext=(0, 0),
                     arrowprops=dict(arrowstyle="-|>", color=col, lw=2, mutation_scale=16))
    ax2.plot(np.cos(t), np.sin(t), color="gray", lw=1, alpha=0.5)
    ax1.set_xlim(-2.2, 2.2)
    ax1.set_ylim(-1.9, 1.9)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title(r"tangents along $\gamma$", fontsize=13)
    ax2.set_xlim(-1.3, 1.3)
    ax2.set_ylim(-1.3, 1.3)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title(r"$\oint_\gamma \kappa\,ds = \tau$", fontsize=13)
    fig.savefig(f"umlaufsatz{suffix}.svg", bbox_inches="tight")
    plt.close()

    # ---------------------------------------------------------------------
    # Fresnel integral as a path (Cornu / Euler spiral)
    from scipy.integrate import cumulative_trapezoid

    T = 7.0
    tt = np.linspace(-T, T, 40001)
    F = cumulative_trapezoid(np.exp(1j * tt**2 / 2), tt, initial=0)
    F = F - F[len(tt) // 2]
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(F.real, F.imag, color=c0, lw=1)
    eye = np.sqrt(tau) / 2 * np.exp(1j * tau / 8)
    ax.annotate("", xy=(eye.real, eye.imag), xytext=(-eye.real, -eye.imag),
                arrowprops=dict(arrowstyle="-|>", color=c1, lw=2.5, mutation_scale=20))
    ax.text(-0.38, 0.22, r"$\sqrt{\tau}\,e^{i\tau/8}$", color=c1, fontsize=14,
            rotation=45, ha="center", va="center")
    tail = -eye
    ax.plot([tail.real, tail.real + 0.9], [tail.imag, tail.imag], color="gray", lw=1, ls="--")
    th = np.linspace(0, tau / 8, 30)
    ax.plot(tail.real + 0.5 * np.cos(th), tail.imag + 0.5 * np.sin(th), color="gray", lw=1)
    ax.text(tail.real + 0.68 * np.cos(tau / 16), tail.imag + 0.68 * np.sin(tau / 16),
            r"$\tau/8$", color="gray", fontsize=11, ha="center", va="center")
    ax.plot([eye.real, -eye.real], [eye.imag, -eye.imag], "o", color=c2, ms=6)
    ax.set_aspect("equal")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.axis("off")
    ax.set_title(r"$x \mapsto \int_{-\infty}^{x} e^{is^2/2}\,ds$", fontsize=14)
    fig.savefig(f"fresnel{suffix}.svg", bbox_inches="tight")
    plt.close()

    # ---------------------------------------------------------------------
    # sin(13.7 tau): 13 full turns plus 0.7 of a turn
    frac = 0.7
    alpha = 13.7 * tau
    fig, ax = plt.subplots(figsize=(5, 5))
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    c0, c1, c2, c3 = colors[0], colors[1], colors[2], colors[3]
    t = np.linspace(0, tau, 400)
    ax.plot(np.cos(t), np.sin(t), color="gray", lw=1, alpha=0.6)
    ax.plot([-1.15, 1.15], [0, 0], color="gray", lw=1, ls="--", alpha=0.6)
    ax.plot([0, 0], [-1.15, 1.15], color="gray", lw=1, ls="--", alpha=0.6)
    x, y = np.cos(alpha), np.sin(alpha)
    # the 0.7 of a turn, as an arc with an arrow head
    ta = np.linspace(0, frac * tau, 300)
    ax.plot(1.08 * np.cos(ta), 1.08 * np.sin(ta), color=c1, lw=2.5)
    ax.annotate(
        "",
        xy=(1.08 * np.cos(frac * tau), 1.08 * np.sin(frac * tau)),
        xytext=(1.08 * np.cos(frac * tau - 0.02), 1.08 * np.sin(frac * tau - 0.02)),
        arrowprops=dict(arrowstyle="-|>", color=c1, lw=2, mutation_scale=22),
    )
    ax.text(1.25 * np.cos(frac * tau / 2), 1.25 * np.sin(frac * tau / 2),
            r"$0.7\,\tau$", color=c1, ha="center", va="center", fontsize=14)
    # radius, sine and cosine
    ax.plot([0, x], [0, y], color=c3, lw=2.5)
    ax.plot([x, x], [0, y], color=c0, lw=3)
    ax.plot([0, x], [0, 0], color=c2, lw=3)
    ax.plot(x, y, "o", color=c3, ms=8)
    ax.text(x + 0.06, y / 2, r"$\sin$", color=c0, ha="left", va="center", fontsize=14)
    ax.text(x / 2, 0.08, r"$\cos$", color=c2, ha="center", va="bottom", fontsize=14)
    ax.set_aspect("equal")
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.axis("off")
    ax.set_title(r"$\sin(13.7\,\tau) \approx -0.95$: 13 turns, then $0.7$ of a turn", fontsize=12)
    fig.savefig(f"sin137{suffix}.svg", bbox_inches="tight")
    plt.close()
