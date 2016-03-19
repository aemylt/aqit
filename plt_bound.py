import math

import matplotlib.pyplot as plt

ys = []
for x in range(2, 1000, 2):
    ys.append(math.log((2**x)/(math.sqrt(x) * (1.99**x)), 2)/x)
    if len(ys) > 1 and ys[-2] > 0.0007:
        assert(ys[-1] > 0.0007)

plt.plot(range(2, 1000, 2), ys)
plt.show()
