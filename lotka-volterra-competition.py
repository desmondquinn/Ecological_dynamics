#Lotka - Volterra competition model
#two species competing for common resources
#one drives the other to extinction
#which species thrives and which goes extinct depend in the starting parameters

import numpy as np
import matplotlib.pyplot as plt


#define parameters
#carrying capacities
k1=35
k2=25
#interaction coefficients
a12=2
a21=0.5
#growth rates
r1=0.2
r2=0.3

# model parameters
dt = 0.1
max_time = 10

# initial time and populations
t = 0 
x = 4.242
y = 3

#create empty list for time and populations
t_list = []
x_list = []
y_list = []

# initialize lists
t_list.append(t) 
x_list.append(x) 
y_list.append(y)

#find x and y at different timesteps (basically euler method)
while t < max_time:
    # calc new values for t, x, y
    t = t + dt
    #updating population values using Lotka Volterra equation
    x = x + r1*x*((k1-x-a12*y)/k1)
    y = y + r2*y*((k2-y-a21*x)/k2)
    # store new values in lists
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

#for phase potrait
    
#define the points to form the meshgrid
xdom = np.linspace(0,42,42);
ydom = np.linspace(0,42,42);
#generate the mesh
[X,Y] = np.meshgrid(xdom,ydom) 
U = r1*X*((k1-X-a12*Y)/k1)
V = r2*Y*((k2-Y-a21*X)/k2)
slice_interval = 4
skip = (slice(None, None,slice_interval),slice(None,None,slice_interval))
#to normalise the lenght of the arrows
M = (np.hypot(U, V))
U = U/M
V = V/M

#plotting the phase portrait
plt.figure(1)
plt.quiver(X[skip], Y[skip], U[skip], V[skip], scale=20, color='blue')
plt.xticks(np.arange(0, 45, 5))
plt.yticks(np.arange(0, 45, 5))
plt.xlabel('population of species 1')
plt.ylabel('population of species 2')
plt.title('Phase portrait')
plt.show()

#plotting the change in populations over time
plt.figure(2)
plt.plot(t_list,x_list, "-b", label="species 1")
plt.plot(t_list, y_list,"-r", label="species 2")
plt.legend(loc="upper left")
plt.xlim(0,10)
plt.ylim(-1,30)
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Population dynamics of the system')
plt.show()


