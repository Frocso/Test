import numpy as np
import matplotlib.pyplot as plt

def f(x):
  a = x**2
  return a

x = np.linspace(0,100,1000)
y = f(x)

plt.plot(x,y)
plt.show()
