import matplotlib.pyplot as plt


#define parameters
b = 0.00015
v = 0.07
dt = 1
max_time = 120

# initial time
t = 0
# initial populations
s = 975
i = 20
r = 5

# empty lists in which to store time and populations
t_list = []
s_list = []
i_list = []
r_list = []
# initialize lists
t_list.append(t)
s_list.append(s)
i_list.append(i)
r_list.append(r)

#find x and y at different timesteps (basically euler method)
while t < max_time:
    # calc new values for t, x, y
    t = t + dt
    s = s + (-b*s*i)*dt
    i = i + (b*s*i - v*i)*dt
    r = r + (v*i)*dt

    # store new values in lists
    t_list.append(t)
    s_list.append(s)
    i_list.append(i)
    r_list.append(r)

# Plot the results    
plt.figure(1)
#p = plt.plot(t_list, x_list, 'r', t_list, y_list, 'g', linewidth = 2)
plt.plot(t_list,s_list, "-b", label="s")
plt.plot(t_list, i_list,"-r", label="i")
plt.plot(t_list, r_list,"-g",label = "r")
plt.legend(loc="upper right")
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Model dynamics')
plt.show()
