import numpy as np
import matplotlib.pyplot as plt
import random

apple = 17

x = np.linspace(0,1,10)
y = np.linspace(0,random.randint(3,9),10)


plt.errorbar(x,y, fmt='o')

