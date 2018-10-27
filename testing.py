import numpy as np
from pprint import pprint as pprint
import datetime
import time


vector1 = np.arange(50000)
vector2 = np.arange(50000)
# matrix1 = np.arange(500000000).reshape(500,1000000)

# pprint(vector1)
# print(matrix1)

# start = datetime.datetime.now()
# # print(np.dot(vector1*matrix1))
# # print(end - start)



check = int(round(time.time() * 1000))

# print(np.array([np.dot(row,vector1) for row in matrix1]))
# check2 = int(round(time.time() * 1000))
# print(check2 - check)
#
# print(np.dot(matrix1,vector1))
# check3 = int(round(time.time() * 1000))
# print(check3 - check2)


# print(np.sum(matrix1*vector1,axis=1))
# check4 = int(round(time.time() * 1000))
# print(check4 - check3)

print(np.sum(vector1,vector2))
check2 = int(round(time.time() * 1000))
print(check2 - check)

# print(np.dot(vector1,vector2))
# check2 = int(round(time.time() * 1000))
# print(check2 - check)

# print(np.array([v1*v2 for v1,v2 in zip(vector1,vector2)]).sum())
# check3 = int(round(time.time() * 1000))
# print(check3 - check2)