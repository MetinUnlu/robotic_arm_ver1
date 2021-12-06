import numpy as np
import math


rot=math.radians(45)

"""
### For rotation around y axis
rotation_matrix= np.array([
   [math.cos(rot), 0, math.sin(rot)],
   [0, 1, 0],
   [-math.sin(rot), 0, math.cos(rot)]
])
"""

"""
### For rotation around z axis
rotation_matrix= np.array([
   [math.cos(rot), -math.sin(rot),0 ],
   [math.sin(rot), math.cos(rot), 0],
   [0, 0, 1]
])
"""
"""
### For rotation around x axis
rotation_matrix= np.array([
   [1, 0,0],
   [0, math.cos(rot), -math.sin(rot)],
   [0, math.sin(rot), math.cos(rot)]
])
"""

rotation_matrix= np.array([
   [1, 0,0],
   [0, math.cos(rot), -math.sin(rot)],
   [0, math.sin(rot), math.cos(rot)]
])


translation= np.array([
    [-12],
    [3],
    [10]
])

P1=np.array([
    [-2],
    [6],
    [-5]
])


P2_transformation_matrix=np.vstack((rotation_matrix,np.array([0,0,0])))
P2_transformation_matrix=np.hstack((P2_transformation_matrix,np.vstack((translation,1))))
P2_transformation_matrix=np.dot(P2_transformation_matrix,np.vstack((P1,1)))

P2_matrix=np.delete(P2_transformation_matrix,3,0)
print(P2_matrix)