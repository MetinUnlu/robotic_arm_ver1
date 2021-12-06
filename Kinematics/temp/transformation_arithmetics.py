import numpy as np
import math


def rotation(rot, rot_axis):
    """
    Takes angle in degrees for the first value, and "x", "y" or "z" input for axis of rotation for the second value.
    """
    rot=math.radians(rot)
    if rot_axis == "x":
        rotation_matrix= np.array([
            [1, 0,0],
            [0, math.cos(rot), -math.sin(rot)],
            [0, math.sin(rot), math.cos(rot)]
        ])
        return(rotation_matrix)
    if rot_axis == "y":
        rotation_matrix= np.array([
            [math.cos(rot), 0, math.sin(rot)],
            [0, 1, 0],
            [-math.sin(rot), 0, math.cos(rot)]
        ])
        return(rotation_matrix)
    if rot_axis == "z":
        rotation_matrix= np.array([
            [math.cos(rot), -math.sin(rot),0 ],
            [math.sin(rot), math.cos(rot), 0],
            [0, 0, 1]
        ])
        return(rotation_matrix)
    else:
        print("Usage correct form of rotation function")

    rot=math.radians(rot)
    if rot_axis == "x":
        rotation_matrix= np.array([
            [1, 0,0],
            [0, math.cos(rot), -math.sin(rot)],
            [0, math.sin(rot), math.cos(rot)]
        ])
        return(rotation_matrix)
    if rot_axis == "y":
        rotation_matrix= np.array([
            [math.cos(rot), 0, math.sin(rot)],
            [0, 1, 0],
            [-math.sin(rot), 0, math.cos(rot)]
        ])
        return(rotation_matrix)
    if rot_axis == "z":
        rotation_matrix= np.array([
            [math.cos(rot), -math.sin(rot),0 ],
            [math.sin(rot), math.cos(rot), 0],
            [0, 0, 1]
        ])
        return(rotation_matrix)
    else:
        print("Usage correct form of rotation function")

def transformation(rotation_matrix, relative_translation):
    transformation_matrix=np.vstack((rotation_matrix,np.array([0,0,0])))
    transformation_matrix=np.hstack((transformation_matrix,np.vstack((relative_translation,1))))    
    return(transformation_matrix)
 
def transformation_dot(transformation_matrix, point_matrix):
    new_point_matrix=np.dot(transformation_matrix,np.vstack((point_matrix,1)))
    return(new_point_matrix)

def inverse_transformation(rotation_matrix, relative_translation):
    inverse_transformation=np.vstack((rotation_matrix,np.array([0,0,0])))
    inverse_transformation=np.hstack((inverse_transformation,np.vstack((np.dot((rotation_matrix*(-1)).T,relative_translation),1))))
    return(inverse_transformation)

b_translation= np.array([
    [2],
    [-5],
    [0]
])

c_translation= np.array([
    [6],
    [0],
    [5]
])

Pc=np.array([
    [8],
    [7],
    [9]
])

Pa=np.dot(transformation(rotation(30,"z"),b_translation), transformation_dot(transformation(rotation(60, "x"), c_translation),Pc))

Pa=np.delete(Pa, 3,0)
print(Pa)

b_to_a_matrix=inverse_transformation(rotation(30,"y"),b_translation)
print(b_to_a_matrix)
