import numpy as np
import math


#Rotation around X axis below in degrees
x_rot=0

#Rotation around Y axis below in degrees
y_rot=0

#Rotation around Z axis below in degrees
z_rot=0

x_rotr=math.radians(x_rot)
y_rotr=math.radians(y_rot)
z_rotr=math.radians(z_rot)


a_ry= np.array([
    [math.cos(math.radians(0+x_rot)), 0, math.sin(rot)],
    [math.cos(math.radians(90-x_rot)), 1, 0],
    [-math.sin(rot), 0, math.cos(rot)]
])

b= np.array([
    [3],
    [0],
    [-5]
])


ab_dot=np.dot(a_ry,b)

print(ab_dot)