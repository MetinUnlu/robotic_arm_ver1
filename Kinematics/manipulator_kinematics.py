import numpy as np
import math
import pandas as pd
from pandas.core.frame import DataFrame
import time
pi=math.pi

def DH_parameter_table_creation(length):
    #Given number of manipulator, creates pandas data frame
    df=pd.DataFrame(index=list(range(length)))
    df.index=df.index + 1
    df['alphai_minus']=float(0)
    df['ai_minus']=float(0)
    df['di']=float(0)
    df['deltai']=float(0)
    return(df)

def define_DH_row(df,row,alphai_minus, ai_minus, di, deltai):
    df['alphai_minus'][row]=alphai_minus
    df['ai_minus'][row]=ai_minus
    df['di'][row]=di
    df['deltai'][row]=deltai
    return(df)

def DH_transformation_matrix(df, target_link):
    matrix_array= np.array([
        [math.cos(df['deltai'][target_link]), math.sin(df['deltai'][target_link])*(-1),0,df['ai_minus'][target_link]],
        [math.sin(df['deltai'][target_link])*math.cos(df['alphai_minus'][target_link]), math.cos(df['deltai'][target_link])*math.cos(df['alphai_minus'][target_link]), math.sin(df['alphai_minus'][target_link])*(-1),math.sin(df['alphai_minus'][target_link])*(-1)*df['di'][target_link]],
        [math.sin(df['deltai'][target_link])*math.sin(df['alphai_minus'][target_link]), math.cos(df['deltai'][target_link])*math.sin(df['alphai_minus'][target_link]), math.cos(df['alphai_minus'][target_link]),math.cos(df['alphai_minus'][target_link])*df['di'][target_link]],
        [0,0,0,1]
        ],dtype=object)
    return(matrix_array)

def forward_kinematics_DH(df,frame1,frame2):
    '''
    \nThis function will provide transformation matrix through out the frames
    \nIn order to get transformation matrix from 0th frame to 1st frame, use (df, 0,1)
    \nIn order to get transformation matrix from 0th frame to 3rd frame, use (df, 0,3)
    \nIn order to get transformation matrix from 2nd frame to 3rd frame, use (df,2,3)
    '''
    frame1=frame1+1
    transformation=DH_transformation_matrix(df,frame2)
    while frame2!=frame1:
        transformation=np.dot(DH_transformation_matrix(df,frame2-1),transformation)
        frame2=frame2-1
        if frame2==0:
            break
    return(transformation)

rpr_manipulator=DH_parameter_table_creation(3)

rpr_manipulator=define_DH_row(rpr_manipulator,1,0,0,0,pi/8)
rpr_manipulator=define_DH_row(rpr_manipulator,2,pi/2,0,2,0)
rpr_manipulator=define_DH_row(rpr_manipulator,3,0,0,5,pi/4)
start_time=time.time()

print(rpr_manipulator)

forward_trial=forward_kinematics_DH(rpr_manipulator,1,3)
print(forward_trial)

print((time.time()-start_time)*1000)
