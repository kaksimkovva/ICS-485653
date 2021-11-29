import math
from numpy import *
import matplotlib.pyplot as plt

x = linspace(1, 10, 1000)
y = x**sin(10*x)

plt.title('My first plot')
plt.plot(x, y)
plt.show()