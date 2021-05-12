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

plt.title("Constant Electric Field")
plt.xlabel("x[m]")
plt.ylabel("y[m]")

plt.show()

"""
PART A 4-7
"""   
def pointChargeFieldAt0(x, y):
    try:
        rSquared = x**2 + y**2
        k = 8.988 * (10**9)
        q = 63 * (10**-9)
        denom = rSquared**1.5
        resultX = (k*q*x)/denom
        resultY = (k*q*y)/denom
        return (resultX, resultY)
    except ZeroDivisionError:
        return (0,0)

k = 8.988 * (10**9)
q = 63 * (10**-9)
x = np.arange(-10,10,1) #setting a range for x values
y = np.arange(-10,10,1) #setting a range for y values

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

u,v = pointChargeFieldAt0(X, Y)

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v)

potential = (k*q)/((X**2 + Y**2)**0.5)

ax.contour(X, Y, potential)

plt.title("Point Charge Field At 0")
plt.xlabel("x[m]")
plt.ylabel("y[m]")

plt.show()

"""
PART A 8
"""
def pointChargeFieldAtAB(x, y, a, b):
    try:
        rSquared = (x-a)**2 + (y-b)**2
        k = 8.988 * (10**9)
        q = 63 * (10**-9)
        denom = rSquared**1.5
        resultX = (k*q*(x-a))/denom
        resultY = (k*q*(y-b))/denom
        return (resultX, resultY)
    except ZeroDivisionError:
        return (0,0)

x = np.arange(-10,13,1) #setting a range for x values
y = np.arange(-10,13,1) #setting a range for y values

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

A = 3
B = 4

u,v = pointChargeFieldAtAB(X, Y, A, B)

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v)

potential = (k*q)/(((X-A)**2 + (Y-B)**2)**0.5)

ax.contour(X, Y, potential)

plt.title("Point Charge Field At A,B")
plt.xlabel("x[m]")
plt.ylabel("y[m]")

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
d = 2 * (10**-6)
x = np.arange(-3*d,3*d,0.2*d) #setting a range for x values
y = np.arange(-3*d,3*d,0.2*d) #setting a range for y values

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

u,v = electricDipoleField(X, Y, d)

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v, scale = 1.2*(10**16))

k = 8.988 * (10**9)
q = 63 * (10**-9)

p1 = (k*q)/(((X**2 + Y**2)**0.5) - d/2)
p2 = (k*q)/(((X**2 + Y**2)**0.5) + d/2)
potential = p1 - p2

ax.contour(X, Y, potential)

plt.title("Electric Dipole Field")
plt.xlabel("x[m]")
plt.ylabel("y[m]")

plt.show()


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
d = 2 * (10**-6)
r = np.arange(-10*d, 10*d, d) 

plt.plot(r, electricDipolePotential(r, d), label="DipolePotential")
plt.plot(r, pointChargePotential(r), label="pointChargePotential")

plt.title("Potential graph for distance")
plt.xlabel("r[m]")
plt.ylabel("phi[V]")
plt.legend()

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

d = 2 * (10**-6)
x = np.arange(0,4*d,0.2*d) #setting a range for x values
y = np.arange(0,4*d,0.2*d) #setting a range for y values

X,Y = np.meshgrid(x, y) #creating a grid for x and y values

u,v = imageCharge(X, Y)

fig, ax = plt.subplots() #creating the figure

ax.quiver(X,Y,u,v, scale = 1.5*(10**16))

plt.title("Image Charge")
plt.xlabel("x[m]")
plt.ylabel("y[m]")

plt.show()

"""
PART C 5
"""
def chargeDensity(y):
    d = 2 * (10**-6)
    q = 63 * (10**-9)
    pi = 3.14
    a = (q*d)/(2*pi)
    bDenom = (d**2 + ((y+d)**2))**1.5
    cDenom = (d**2 + ((y-d)**2))**1.5
    return a*((1/bDenom)-(1/cDenom))

"""
PART C 6
"""
d = 2 * (10**-6)
y = np.arange(0, 10*d, 0.1*d) #setting a range for x values
plt.plot(y, chargeDensity(y)) #creating the figure
plt.title("Charge Density")
plt.xlabel("y[m]")
plt.ylabel("sigma[C/m^2]")
plt.show()
