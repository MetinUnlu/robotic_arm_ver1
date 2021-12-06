from numpy import *

arr1 = array ([ 
    [2,3,4],
    [12,15,17],
    [22,26,28]
])


print(arr1)

arr1_det=linalg.det(arr1)

print ("\nDeterminant:", arr1_det)

arr1_inv=linalg.inv(arr1)

print("\nInverse:")

print(arr1_inv)