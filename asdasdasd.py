#pip install matplotlib --proxy http://tanulo01:Tanulo0118@172.16.0.5:8080

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 50])
ypoints = np.array([0, 0])

#plt.plot(xpoints, ypoints)
#plt.plot([0,0],[50,10])
#plt.show()


x=[0,50,50,0,0]
y=[0,0,50,50,0]
plt.plot(x, y)

plt.show()


