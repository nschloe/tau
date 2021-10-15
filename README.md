# tau


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

ndim
https://github.com/nschloe/ndim#the-formulas

Wikipedia:
Proposals for a single letter to represent 2π
https://en.wikipedia.org/wiki/Turn_(angle)#Tau_proposals

#### Some equations
The following equations are best consumed on Chrome with
[xdoc](https://chrome.google.com/webstore/detail/xdoc/anidddebgkllnnnnjfkmjcaallemhjee)
installed.

- Trigonometrics
```math
\sin(\alpha) = \sin(\alpha + \tau) \forall \alpha\\
\cos(\alpha) = \cos(\alpha + \tau) \forall \alpha\\
\tan(\alpha) = \tan(\alpha + \tau) \forall \alpha
```

```math
\tau^{-1/2} \int_{-\infty}^{\infty} \exp\left(-\frac{1}{2} x^2\right) = 1
```

- Area of the _n_-dimensional unit sphere (recurrence)
```math
|U_n| = \begin{cases}
2 & \text{if } n = 1\\
\tau & \text{if } n = 2\\
|U_{n-2}| \times \frac{\tau}{n-2}
\end{cases}
```

- Area of the _n_-dimensional unit ball (recurrence)
```math
|S_n| = \begin{cases}
1 & \text{if } n = 0\\
2 & \text{if } n = 1\\
|S_{n-2}| \times \frac{\tau}{n}
\end{cases}
```
- more such examples at [ndim](https://github.com/nschloe/ndim)

- Cauchy's integral formula
```math
f(a) = \frac{1}{i\tau} \oint \frac{f(z)}{z - a} \,dz
```

- Fourier transform
```math
\hat{f}(\xi) &= \int_{-\infty}^{\infty} f(x) \exp(-i\tau x\xi)\,dx,\\
f(x)         &= \int_{-\infty}^{\infty} \hat{f}(\xi) \exp(i\tau x\xi)\,d\xi
```

Harder:
```math
\int_{-\infty}^{\infty} \exp(-x^2) = \sqrt{\pi}
```
