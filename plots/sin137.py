import matplotlib.pyplot as plt
from math import tau, sin, cos, sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.transforms import IdentityTransform, TransformedBbox, Bbox


fig, ax = plt.subplots()

# plt.axis('off')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_color("0.8")
ax.spines['bottom'].set_color("0.8")
ax.spines['bottom'].set_color("0.8")
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])
ax.tick_params(axis='x', colors='0.8')
ax.tick_params(axis='y', colors='0.8')

# plt.grid(True, color="0.9")

circle1 = plt.Circle((0, 0), 1.0, color="0.8", fill=False)
ax.add_patch(circle1)

# plt.plot([-1.5, 1.5], [0.0, 0.0], "0.8")
# plt.plot([0.0, 0.0], [-1.5, 1.5], "0.8")

x = cos(13.7 * tau)
y = sin(13.7 * tau)
a = sqrt(x**2 + y**2)
x /= a
y /= a

plt.plot([x, x], [0.0, y], ":", color="0.7")
plt.plot([0.0, x], [y, y], ":", color="0.7")

lw = 2.0
plt.plot([0.0, 0.0], [0.0, y], "tab:blue", linewidth=lw, zorder=5)
plt.plot([0.0, x], [0.0, 0.0], "tab:red", linewidth=lw, zorder=5)
plt.plot([0.0, x], [0.0, y], "tab:purple", linewidth=lw, zorder=5)

# arc1 = Arc((0.0, 0.0), 0.15, 0.15, theta1=0.0, theta2=0.7 * 360, color="purple")
# ax.add_patch(arc1)
arc2 = Arc((0.0, 0.0), 2.0, 2.0, theta1=0.0, theta2=0.7 * 360, color="tab:purple", zorder=5, linewidth=lw)
ax.add_patch(arc2)

ax.annotate(r"$\cos(\alpha)$", [x / 2 - 0.1, 0.05], color="tab:red")
ax.annotate(r"$\sin(\alpha)$", [0.05, y / 2], color="tab:blue")

ax.set_aspect("equal")
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

plt.savefig("sin137.svg", bbox_inches="tight")
# plt.show()
