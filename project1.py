import matplotlib.pyplot as plt
import numpy as np

"""
PART A 1-3
"""
x = np.arange(-50,50,5) #setting a range for x values
y = np.arange(-50,50,5) #setting a range for y values

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

u = 0 #setting the direction for x axis
v = 1 #setting the direction for y axis

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v) 

plt.show()

"""
PART A 4-7
"""
def pointChargeFieldAt0(x, y):
    try:
        rSquared = x**2 + y**2
        k = 8.988 * (10**9)
        q = 63 * (10**-9)
        point = (k*q)/rSquared
        theta = np.arctan2(y,x);
        resultX = point * np.cos(theta)
        resultY = point * np.sin(theta)
        return (resultX, resultY)
    except ZeroDivisionError:
        return (0,0)

x = np.arange(-10,10,1) #setting a range for x values
y = np.arange(-10,10,1) #setting a range for y values

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

u,v = pointChargeFieldAt0(X, Y)

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v)

#contour(X,Y)

plt.show()

"""
PART A 8
"""
def pointChargeFieldAtAB(x, y, a, b):
    try:
        rSquared = (x-a)**2 + (y-b)**2
        k = 8.988 * (10**9)
        q = 63 * (10**-9)
        point = (k*q)/rSquared
        theta = np.arctan2(y,x);
        resultX = point * np.cos(theta)
        resultY = point * np.sin(theta)
        return (resultX, resultY)
    except ZeroDivisionError:
        return (0,0)

A,B = 3,4
x = np.arange(-10-A,10+A,1) #setting a range for x values
y = np.arange(-10-B,10+B,1) #setting a range for y values

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

u,v = pointChargeFieldAtAB(X, Y, 1, 2)

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v)

#contour(X,Y)

plt.show()
    
"""
PART B 2
"""
def electricDipoleField(x, y, d):
    x1,y1 = pointChargeFieldAtAB(x, y, d/2, 0)
    x2,y2 = pointChargeFieldAtAB(x, y, -d/2, 0)
    resultX = x1 - x2
    resultY = y1 - y2
    return (resultX, resultY)

"""
PART B 3-4
"""
x = np.arange(-10,10,1) #setting a range for x values
y = np.arange(-10,10,1) #setting a range for y values
d = 2 * (10**-6)

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

u,v = electricDipoleField(X, Y, d)

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v)

#plt.contour(X,Y,Z)

plt.show()

"""
PART B 5
"""
# contour(X,Y,Z) - potential lines

"""
PART B 7
"""
def electricDipolePotential(r, d):
    p1 = pointChargePotential(r - d/2)
    p2 = pointChargePotential(r + d/2)
    return p1-p2

"""
PART B 8
""" 
def pointChargePotential(r):
    try:
        k = 8.988 * (10**9)
        q = 63 * (10**-9)
        point = (k*q)/r
        return point
    except ZeroDivisionError:
        return (0,0)

"""
PART B 9
"""
r = np.arange(-1,1,0.1) #setting a range for x values
d = 2 * (10**-6)
plt.plot(r, electricDipolePotential(r, d)) #creating the figure
plt.show()

"""
PART C 3
"""
def imageCharge(x, y):
    try:
        d = 2 * (10**-6)
        k = 8.988 * (10**9)
        q = 63 * (10**-9)
        e1x, e1y = pointChargeFieldAtAB(x, y, d, d)
        e2x, e2y = pointChargeFieldAtAB(x, y, -d, d)
        e3x, e3y = pointChargeFieldAtAB(x, y, -d, -d)
        e4x, e4y = pointChargeFieldAtAB(x, y, d, -d)
        resultX = e1x - e2x + e3x - e4x
        resultY = e1y - e2y + e3y - e4y
        return (resultX, resultY)
    except ZeroDivisionError:
        return (0,0)


x = np.arange(0,10,0.5) #setting a range for x values
y = np.arange(0,10,0.5) #setting a range for y values

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

u,v = imageCharge(X, Y)

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v)

plt.show()
