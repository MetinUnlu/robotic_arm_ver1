import numpy as np
import math

rot=math.radians(60)


a_ry= np.array([
    [math.cos(rot), 0, math.sin(rot)],
    [0, 1, 0],
    [-math.sin(rot), 0, math.cos(rot)]
])

b= np.array([
    [3],
    [0],
    [-5]
])


ab_dot=np.dot(a_ry,b)

print(ab_dot)