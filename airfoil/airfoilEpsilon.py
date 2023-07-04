import matplotlib.pyplot as plt
from math import cos,sin

#variables
x_point_up = []
y_point_up = []
x_point_down = []
y_point_down = []
epsilon_x = []
epsilon_y = []
bg_x = []
bg_y = []
r_down = 0
r_up = 0

#declare the quanitites
cex = 4.5
cey = 5.0
theta = 0.0
length = 1.0
nxn = 2001
nyn = 2001
lx = 10
ly = 10

dx = lx/nxn
dy = ly/nyn

print("dx=",dx," and dy=",dy)
print("Reading Data")

#reading data from dat file
for m in open('airfoil_up.dat').readlines():
	l = m.strip().split()
	x_point_up.append(float(l[0]))
	y_point_up.append(float(l[1]))

for m in open('airfoil_down.dat').readlines():
	l = m.strip().split()
	x_point_down.append(float(l[0]))
	y_point_down.append(float(l[1]))

print("Reading Data finished !")
#main program
for j in range(nyn):
	ym = dy*j
	for i in range(nxn):
		xm =dx*i
		#change of origin
		xmnew = xm-cex
		ymnew = ym-cey
		#rotation of coordinate system to account for AOA
		x = xmnew*cos(theta) - ymnew*sin(theta)
		y = xmnew*sin(theta) + ymnew*cos(theta)

		if(x<length):
			for n in range(1, len(x_point_up)-2):
				if (x/length <x_point_up[n+1] and x/length>x_point_up[n]):
					r_up = length * (y_point_up[n+1]-y_point_up[n])/(x_point_up[n+1]-x_point_up[n])*((x/length)-x_point_up[n])
				if (x/length >x_point_down[n+1] and x/length<x_point_down[n]):
					r_down = length * (y_point_down[n+1]-y_point_down[n])/(x_point_down[n+1]-x_point_down[n])*((x/length)-x_point_down[n])
	
			if(y>=r_down and y<=r_up):
				epsilon_x.append(x)
				epsilon_y.append(y)
			else:
				bg_x.append(x)
				bg_y.append(y)

print("Epsilon Function determined, plotting in progress..")
print(epsilon_x)
#plotting the epslion function
plt.scatter(epsilon_x,epsilon_y)
#plt.scatter(bg_x,bg_y,color='red')
#plt.scatter(5*x_point_up,5*y_point_up,color='black')
#plt.scatter(5*x_point_down,5*y_point_down,color='black')
plt.show()