import numpy as np
import math
from math import cos,sin,tanh
pi=math.pi

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

def multi_rotation(orderofrotation,gamma,beta,alpha):
    '''Order of rotation ex: "xyz", or "yzx" and similar
    \ngamma for rotation around X-axis,
    \nbeta for rotation around Y-axis,
    \nalpha for rotation around Z-axis.
    '''
    x_matrix=rotation(gamma, "x")
    y_matrix=rotation(beta, "y")
    z_matrix=rotation(alpha, "z")
    if orderofrotation=="xyz":
        rotation_matrix=np.dot(z_matrix,np.dot(y_matrix,x_matrix))
    if orderofrotation=="yxz":
        rotation_matrix=np.dot(z_matrix,np.dot(x_matrix,y_matrix))
    if orderofrotation=="zyx":
        rotation_matrix=np.dot(x_matrix,np.dot(y_matrix,z_matrix))
    if orderofrotation=="yzx":
        rotation_matrix=np.dot(x_matrix,np.dot(z_matrix,y_matrix))
    if orderofrotation=="zxy":
        rotation_matrix=np.dot(y_matrix,np.dot(x_matrix,z_matrix))
    if orderofrotation=="xzy":
        rotation_matrix=np.dot(y_matrix,np.dot(x_matrix,z_matrix))
    return(rotation_matrix)

def angles_of_fixedxyz_matrix(matrix):
    r=matrix
    beta=math.atan2(r[2,0]*(-1),(math.sqrt(r[0,0]**2+r[1,0]**2)))
    alpha=math.atan2(r[1,0]/math.cos(beta),r[0,0]/math.cos(beta))
    gamma=math.atan2(r[2,1]/math.cos(beta),r[2,2]/math.cos(beta))
    print("Beta= ",math.degrees(beta), "°", "\nAlpha= ", math.degrees(alpha),"°", "\nGamma= ", math.degrees(gamma),"°")

def transformation(rotation_matrix, relative_translation):
    transformation_matrix=np.vstack((rotation_matrix,np.array([0,0,0])))
    transformation_matrix=np.hstack((transformation_matrix,np.vstack((relative_translation,1))))    
    return(transformation_matrix)
 
def transformation_dot(transformation_matrix, point_matrix):
    new_point_matrix=np.dot(transformation_matrix,np.vstack((point_matrix,1)))
    return(new_point_matrix)

def inverse_transformation(rotation_matrix, relative_translation):
    inverse_transformation=np.vstack((rotation_matrix.T,np.array([0,0,0])))
    inverse_transformation=np.hstack((inverse_transformation,np.vstack((np.dot((rotation_matrix*(-1)).T,relative_translation),1))))
    return(inverse_transformation)

def inverse_given_matrix(matrix):
    rotation_matrix=np.delete(np.delete(matrix, 3, 0),3,1)
    translation_matrix=np.delete(np.delete(matrix,np.s_[0:3],1),3,0)
    inverse_matrix=inverse_transformation(rotation_matrix, translation_matrix)
    return(inverse_matrix)

def euler_to_rotation(roll,pitch,yaw):
    roll=math.radians(roll)
    print(roll)
    pitch=math.radians(pitch)
    yaw=math.radians(yaw)
    rotation_matrix=np.array([  [cos(roll)*cos(pitch), cos(roll)*sin(pitch)*sin(yaw)-sin(roll)*cos(yaw), cos(roll)*sin(pitch)*cos(yaw)+sin(roll)*sin(yaw)],
                                [sin(roll)*cos(pitch), sin(roll)*sin(pitch)*sin(yaw)+cos(roll)*cos(yaw), sin(roll)*sin(pitch)*cos(yaw)-cos(roll)*sin(yaw)],
                                [-sin(pitch),cos(pitch)*sin(yaw),cos(pitch)*cos(yaw)]
                                ])
    return rotation_matrix

transformation_matrix=np.array([
    [0.866, 0.5, 0, -4.964],
    [-0.5, 0.866, 0, -0.598],
    [0,0,1,0],
    [0,0,0,1]
])

ba_translation= np.array([
    [-4.964],
    [-0.598],
    [0]
])

bc_translation= np.array([
    [0],
    [0],
    [0]
])

rotation_matrix=np.array([
    [0.9077, -0.2946, 0.2989],
    [0.3304, 0.9408, -0.0760],
    [-0.2588,0.1677,0.9513]
])

#print(angles_of_fixedxyz_matrix(rotation_matrix))

ab_transformation=inverse_given_matrix(transformation_matrix)
#print(ab_transformation)
bc_transformation=transformation(rotation(22.5,"z"),bc_translation)
print("The transformation matrix is:")
print(bc_transformation)
ac_transformation=np.dot(ab_transformation,bc_transformation)
#print(ac_transformation)


