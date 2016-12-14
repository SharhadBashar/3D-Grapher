# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import itertools
import random, glob
import matplotlib.cm as cm, IPython.display as IPdisplay 
from mpl_toolkits.mplot3d import axes3d, Axes3D

data = np.genfromtxt('C:input_path.csv',skiprows = 1, delimiter=',')

Px=data[:,7]
Py=data[:,8]
Pz=data[:,9]




ps = [(ts,x,y,z,fx,fy,fz) for (ts,x,y,z,fx,fy,fz) in zip(t_dsr,x_dsr_norm, y_dsr_norm, z_dsr_norm, fx_dsr, fy_dsr, fz_dsr)]
for start, end in zip(ps[:-1], ps[1:]):
    ts, x, y, z, fx, fy, fz = zip(start, end)

########### Draws graph ####################
fig = plt.figure(figsize=(12,21))

ax1 = plt.subplot2grid((15, 3), (0, 0), colspan=3, rowspan=3, projection='3d')
ax1.plot(Px,Py,Pz,)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.autoscale()

plt.show
##################################################

