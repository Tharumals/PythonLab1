import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0,(math.pi)/2,0.1)
print(x)

y = np.dot(5,np.sin(x)) - 12

t = np.arange(0,5,0.1)

f = 2*t+3

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')
plt.plot(t,f, 's')

# show the plot
plt.show()
