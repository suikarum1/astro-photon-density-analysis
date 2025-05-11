



'''

x = []
y = []


for ra0 in range(360):
    for dec0 in range(-90,90):
        x.append(ra0)
        y.append(dec0)
        z = func(ra0,dec0)
#接近南北极时取一个点就够了，接近赤道时多取几个
'''

import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator


# setup the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



crimefile = open('x1.txt', 'r')
for line in crimefile.readlines():
    x = line.split(',')
    x = x[:-1]
print(len(x))
x0 = np.array(x).astype(np.float)


crimefile = open('y1.txt', 'r')
for line in crimefile.readlines():
    y = line.split(',')
    y = y[:-1]
print(len(y))
y0 = np.array(y).astype(np.float)


crimefile = open('wwe.txt', 'r')#can be replaced by z_uv.txt
for line in crimefile.readlines():
    z1 = line.split(',')
    z1 = z1[:-1]
print(len(z1))
z0 = np.array(z1).astype(np.float)



dx = dy = 20
bottom1 = np.zeros_like(z0)
#bottom2 = np.zeros_like(z2)
print('success_node1')

cmap = cm.get_cmap('jet')
max_height = np.max(z0)   # get range of colorbars so we can normalize
min_height = np.min(z0)
# scale each z to [0,1], and get their rgb values
rgba = [cmap((k-min_height)/max_height) for k in z0]

ax.bar3d(x0, y0, bottom1, dx, dy, z0, color=rgba, zsort='average')
print('success_node2')
ax.set_title('UV')
plt.show()

#ax.bar3d(x, y, bottom2, dx, dy, z2, shade=True)
#ax.set_title('UV')
#plt.show()
