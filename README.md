# tau

In 2001, Bob Palais wrote the article _Pi is wrong!_, remarking on the fact that
whenever π occurs in nature, it occurs as 2π most of the time. He suggests that
2π=6.283185... should be given a name (τ is now a fan favorite) and that it should be
used instead of π. Some found his arguments convincing, and the τ movement was born.

This page lists notable articles, videos, discussion etc. about τ.

#### Articles and blog posts

- [Bob Palais, _π is wrong!_, 2001](https://doi.org/10.1007%2FBF03026846)

- [Michael Hartl, _The Tau Manifesto_, 2010](https://tauday.com/tau-manifesto)
  As paperback [on Amazon](https://www.amazon.com/Tau-Manifesto-No-really-pi-is-wrong/dp/B096CXMQ3W/)

- [Randyn Charles Bartholomew, _Let's Use Tau--It's Easier Than Pi_, 2014](https://www.scientificamerican.com/article/let-s-use-tau-it-s-easier-than-pi/)

- [Giorgia Fortuna, _2 Pi or Not 2 Pi?_, 2015](https://blog.wolfram.com/2015/06/28/2-pi-or-not-2-pi/)

- [Stephen Abbott, _Aftermath: My Conversion to Tauism_, 2018](https://doi.org/10.4169%2Fmathhorizons.19.4.34)

- <a href="https://en.wikipedia.org/wiki/Turn_(angle)#Tau_proposals">Wikipedia, <emph>Proposals for a single letter to represent 2π</emph></a>

#### Videos

- [Vihart, _Pi Is (still) Wrong_, 2011](https://youtu.be/jG7vhMMXagQ)
- [Numberphile, _Tau vs Pi Smackdown_, 2012](https://youtu.be/ZPv1UV0rD8U)

#### In pop culture

- [XKCD, _Pi vs. Tau_](https://xkcd.com/1292/)
- [Tau Day, June 28, 6/28](https://www.google.com/search?q=tau+day)

#### In programming

- [Python, since 3.6 (2016)](https://www.python.org/dev/peps/pep-0628/)
- [.NET, C#, since 5.0 (2016)](https://docs.microsoft.com/en-us/dotnet/api/system.math.tau)
- [Rust, since 1.47 (2020)](https://doc.rust-lang.org/std/f64/consts/constant.TAU.html)
- [Processing](https://processing.org/reference/TAU.html)

- [Boost, since 1.77.0 (2021)](https://www.boost.org/doc/libs/1_77_0/boost/math/constants/constants.hpp)

Inclusion of a constant `tau` was _rejected_ by the following projects:

- [NumPy](https://github.com/numpy/numpy/pull/9696)
- [Julia](https://github.com/JuliaLang/julia/pull/4864)
- [Go](https://github.com/golang/go/issues/40663)

#### Some equations

The following equations are best consumed on Chrome with
[xdoc](https://chrome.google.com/webstore/detail/xdoc/anidddebgkllnnnnjfkmjcaallemhjee)
installed.

- Trigonometrics

  ```math
  \begin{split}
  \sin(\alpha) &= \sin(\alpha + {\color{RubineRed} \tau}) \quad\forall \alpha\\
  \cos(\alpha) &= \cos(\alpha + \tau) \quad\forall \alpha\\
  \tan(\alpha) &= \tan(\alpha + \tau) \quad\forall \alpha
  \end{split}
  ```

  With $`\tau`$ being a full revolution, the following identities are very easy to grasp
  (for integers $`n`$). Remember the sine is the projection of the angle onto the
  _y_-axis, the cosine is the projection onto the _x_-axis.

  ```math
  \begin{alignat*}{3}
    \sin(n \tau) &= 0,          &\qquad \cos(n \tau) &= 1,\\
    \sin((n + 1/4) \tau) &= 1,  &\qquad \cos((n + 1/4) \tau) &= 0,\\
    \sin((n + 1/2) \tau) &= 0,  &\qquad \cos((n + 1/2) \tau) &= -1,\\
    \sin((n + 3/4) \tau) &= -1, &\qquad \cos((n + 3/4) \tau) &= 0
  \end{alignat*}
  ```

  Trigonometric values off the grid can easily be estimated:

  - $`\sin(13.7 \pi)`$ – Where is my calculator?
  - $`\sin(13.7 \tau)`$ – 13 full revolutions: forget about those. Plus .7, that's
    almost 3/4 of a revolution, so probably something close to -1.

- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)

  ```math
  \int_{-\infty}^{\infty} \frac{1}{\sigma \sqrt{\tau}} \exp\left(-\frac{(x-\mu)^2}{2 \sigma^2}\right) = 1
  ```

  But:
  ```math
  \int_{-\infty}^{\infty} \exp(-x^2) = \sqrt{\pi}
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
