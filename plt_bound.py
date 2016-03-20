import math

import matplotlib.pyplot as plt

ys = []
for x in range(2, 1002, 2):
    ys.append(math.log((2**x)/(math.sqrt(x) * (1.99**x)), 2))
    if len(ys) > 1 and ys[-2] > 0.0007*(x-2):
        assert(ys[-1] > 0.0007*x)
    elif ys[-1] > 0.0007*x:
        print(x)

plt.plot(range(2, 1002, 2), ys, label=r'$y = \log_2(2^n/(1.99^n*\sqrt{n}))$')
plt.plot(range(2, 1002, 2), [0.0007 * x for x in range(2, 1002, 2)], label=r'$y = 0.0007n$')
plt.title(r'$y = \log_2(2^n/(1.99^n*\sqrt{n}))$ against $y = 0.0007n$ for even values of $n$ from $2$ to $1000$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend(loc=2)
plt.show()
