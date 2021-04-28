import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100,5) #setting a range for x values
y = np.arange(0,100,5) #setting a range for y values

X, Y = np.meshgrid(x, y) #creating a grid for x and y values

u = 0 #setting the direction for x axis
v = 1 #setting the direction for y axis

fig, ax = plt.subplots(figsize=(9,9)) #creating the figure

ax.quiver(X,Y,u,v) 

plt.show()
