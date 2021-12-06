import numpy as np
import math


rot=math.radians(45)

"""
### For rotation around y axis
a_ry= np.array([
   [math.cos(rot), 0, math.sin(rot)],
   [0, 1, 0],
   [-math.sin(rot), 0, math.cos(rot)]
])
"""

"""
### For rotation around z axis
a_ry= np.array([
   [math.cos(rot), -math.sin(rot),0 ],
   [math.sin(rot), math.cos(rot), 0],
   [0, 0, 1]
])
"""

### For rotation around x axis
a_ry= np.array([
   [1, 0,0],
   [0, math.cos(rot), -math.sin(rot)],
   [0, math.sin(rot), math.cos(rot)]
])

b_P= np.array([
    [-2],
    [6],
    [-5]
])

borg=np.array([
    [-12],
    [3],
    [10]
])

ab_dot=np.dot(a_ry,b_P)

a_P=ab_dot+borg


a_b_trans=np.vstack((a_ry,np.array([0,0,0])))
a_b_trans=np.hstack((a_b_trans,np.vstack((borg,1))))
a_b_trans=np.dot(a_b_trans,np.vstack((b_P,1)))

a_P=np.delete(a_b_trans,3,0)
print(a_P)