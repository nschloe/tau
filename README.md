# tau

In 2001, Bob Palais wrote the article _Pi is wrong!_, remarking on the fact that
whenever π occurs in nature, it occurs as 2π most of the time. He suggests that 2π
should be given a name (τ is now a fan favorite) and that this constant should be used
instead of π. Some found his arguments convincing, and the τ movement was born.

This page lists notable articles, videos, discussion etc. about τ.

#### Articles and blog posts

- [Bob Palais, _Pi is wrong!_, 2001](http://www.math.utah.edu/~palais/pi.pdf)

- [Michael Hartl, _The Tau Manifesto_, 2010](https://tauday.com/tau-manifesto)
  As paperback [on Amazon](https://www.amazon.com/Tau-Manifesto-No-really-pi-is-wrong/dp/B096CXMQ3W/)

- [Giorgia Fortuna, _2 Pi or Not 2 Pi?_, 2015](https://blog.wolfram.com/2015/06/28/2-pi-or-not-2-pi/)

#### Videos

- [Vihart, _Pi Is (still) Wrong_, 2011](https://youtu.be/jG7vhMMXagQ)
- [Numberphile, _Tau vs Pi Smackdown_, 2012](https://youtu.be/ZPv1UV0rD8U)

#### In pop culture

- [XKCD, _Pi vs. Tau_](https://xkcd.com/1292/)
- [Tau Day, June 28, 6/28](https://www.google.com/search?q=tau+day&oq=tau+day&aqs=chrome..69i57j69i59j35i39l2j69i60l4.1043j0j7&sourceid=chrome&ie=UTF-8)

#### In programming

- [Python, since 3.6 (2016)](https://www.python.org/dev/peps/pep-0628/)
- [.NET, C#, since 5.0 (2016)](https://docs.microsoft.com/en-us/dotnet/api/system.math.tau)
- [Rust, since 1.47 (2020)](https://doc.rust-lang.org/std/f64/consts/constant.TAU.html)

- [Boost, since 1.77.0 (2021)](https://www.boost.org/doc/libs/1_77_0/boost/math/constants/constants.hpp)

Inclusion of a constant `tau` was _rejected_ by the following projects:

- [NumPy](https://github.com/numpy/numpy/pull/9696)
- [julia](https://github.com/JuliaLang/julia/pull/4864)
- [Go](https://github.com/golang/go/issues/40663)

Wikipedia:
Proposals for a single letter to represent 2π
https://en.wikipedia.org/wiki/Turn_(angle)#Tau_proposals

#### Some equations

The following equations are best consumed on Chrome with
[xdoc](https://chrome.google.com/webstore/detail/xdoc/anidddebgkllnnnnjfkmjcaallemhjee)
installed.

- Trigonometrics

```math
\begin{split}
\sin(\alpha) &= \sin(\alpha + \tau) \quad\forall \alpha\\
\cos(\alpha) &= \cos(\alpha + \tau) \quad\forall \alpha\\
\tan(\alpha) &= \tan(\alpha + \tau) \quad\forall \alpha
\end{split}
```

- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)

```math
f(x) = \frac{1}{\sigma \sqrt{\tau}} \exp\left(-\frac{(x-\mu)^2}{2 \sigma^2}\right)
```

- Area of the _n_-dimensional unit sphere (recurrence)

```math
|U_n| = \begin{cases}
2 & \text{if } n = 1\\
\tau & \text{if } n = 2\\
|U_{n-2}| \times \tau / (n - 2) & \text{otherwise}
\end{cases}
```

- Volume of the _n_-dimensional unit ball (recurrence)

```math
|S_n| = \begin{cases}
1 & \text{if } n = 0\\
2 & \text{if } n = 1\\
|S_{n-2}| \times \tau / n & \text{otherwise}
\end{cases}
```

The area of a disk:
```math
A = \pi r^2 = \frac{1}{2} \tau r^2
```

- more such examples at [ndim](https://github.com/nschloe/ndim)

- [Cauchy's integral formula](https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula)

```math
f(a) = \frac{1}{i\tau} \oint \frac{f(z)}{z - a} \,dz
```

- [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform)

```math
\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) \exp(-i\tau x\xi)\,dx,\quad
f(x)         = \int_{-\infty}^{\infty} \hat{f}(\xi) \exp(i\tau x\xi)\,d\xi
```

- [<emph>n<emph>th roots of unity](https://en.wikipedia.org/wiki/Root_of_unity)

```math
z^n = 1 \quad\Rightarrow\quad z = \exp(\tau i / n)
```

- [Euler's identity](https://en.wikipedia.org/wiki/Euler%27s_identity)

```math
\exp(\pi i) + 1  = 0,\quad
\exp(\tau i) - 1 = 0
```

- [Stirling's approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation)

```math
n! \sim \sqrt{\tau n} \left(\frac{n}{e}\right)^n
```

Harder:

```math
\int_{-\infty}^{\infty} \exp(-x^2) = \sqrt{\pi}
```
