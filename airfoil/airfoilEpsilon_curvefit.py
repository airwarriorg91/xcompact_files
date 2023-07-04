import matplotlib.pyplot as plt
from math import cos,sin,pi
import numpy as np
from scipy.optimize import curve_fit


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
theta_deg = 5.0
length = 2.0
nxn = 2001
nyn = 2001
lx = 10
ly = 10

dx = lx/nxn
dy = ly/nyn
theta = theta_deg * pi/180
print("dx=",dx," and dy=",dy)
print("Reading Data")

#reading data from dat file
for m in open('goe417_up.dat').readlines():
	l = m.strip().split()
	x_point_up.append(float(l[0]))
	y_point_up.append(float(l[1]))

for m in open('goe417_down.dat').readlines():
	l = m.strip().split()
	x_point_down.append(float(l[0]))
	y_point_down.append(float(l[1]))

print("Reading Data finished !")

#curvefiting of the airfoil
x_point_up = length * np.asarray(x_point_up)
x_point_down = length * np.asarray(x_point_down)
y_point_up = length * np.asarray(y_point_up)
y_point_down = length * np.asarray(y_point_down)

def airfoil_eqn(x,A,B,C,D,E,F,G):
	y = A*x**6 + B*x**5 + C*x**4 + D*x**3 + E*x**2 + F*x + G
	return y

#rotation of coordinate system to account for AOA
x_point_up = x_point_up*cos(theta) + y_point_up*sin(theta)
y_point_up = -x_point_up*sin(theta) + y_point_up*cos(theta)

x_point_down = x_point_down*cos(theta) + y_point_down*sin(theta)
y_point_down = -x_point_down*sin(theta) + y_point_down*cos(theta)

parametersup, covariance = curve_fit(airfoil_eqn,x_point_up,y_point_up)
#airfoil_up = airfoil_eqn(x_point_up, parameters[0],parameters[1],parameters[2],parameters[3],parameters[4],parameters[5],parameters[6])

parametersdown, covariance = curve_fit(airfoil_eqn,x_point_down,y_point_down)
#airfoil_down = airfoil_eqn(x_point_down, parameters[0],parameters[1],parameters[2],parameters[3],parameters[4],parameters[5],parameters[6])

#fitting airfoil data finished

#main program
for j in range(nyn):
	ym = dy*j
	for i in range(nxn):
		xm =dx*i
		#change of origin
		x = xm-cex
		y = ym-cey

		if(x<length and x>=0):
			r_up = parametersup[0]*x**6 + parametersup[1]*x**5 + parametersup[2]*x**4 + parametersup[3]*x**3 + parametersup[4]*x**2 + parametersup[5]*x + parametersup[6]
			r_down = parametersdown[0]*x**6 + parametersdown[1]*x**5 + parametersdown[2]*x**4 + parametersdown[3]*x**3 + parametersdown[4]*x**2 + parametersdown[5]*x + parametersdown[6]	
	
			if(y>=r_down and y<=r_up):
				epsilon_x.append(x)
				epsilon_y.append(y)
			'''else:
				bg_x.append(x)
				bg_y.append(y)'''

print("Epsilon Function determined, plotting in progress..")
#print(epsilon_x)
#plotting the epslion function
plt.scatter(epsilon_x,epsilon_y, label='Epsilon')
plt.xlim(-length * 0.1, length * 1.2)
plt.ylim(-length * 0.5,length * 0.5)
#plt.scatter(bg_x,bg_y,color='red')
plt.scatter(x_point_up,y_point_up,color='black', label='Coordinates')
plt.scatter(x_point_down,y_point_down,color='black')
plt.title("GOE417 Airfoil in "+ str(nxn)+"x"+ str(nyn)+" nodes at "+str(theta_deg)+" Deg")
plt.legend()
plt.show()


