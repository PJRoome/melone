import numpy as np
import matplotlib.pyplot as plt

banana = np.pi + 231
apple = 17

x = np.linspace(0,1,10)
y = np.linspace(0,3,10)

plt.errorbar(x,y, fmt='o')

print(banana, apple)
