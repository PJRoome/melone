import numpy as np
import matplotlib.pyplot as plt

banana = np.pi + 231
apple = 17

x = np.linspace(0,1,100)
y = x = np.linspace(0,3,100)

plt.errorbar(x,y)
plt.show()
print(banana, apple)
