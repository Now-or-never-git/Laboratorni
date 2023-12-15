import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100) 

y = -x**np.cos(5*x)

plt.plot(x, y, label='Графік функції $-x^{\cos(5x)}$', color = "blue", linewidth = 2)

plt.title('My plot', fontsize=15) 

plt.xlabel('x', fontsize=12, color='black') 
plt.ylabel('y', fontsize=12, color='black')   
plt.legend()
plt.grid(True)
plt.show()
