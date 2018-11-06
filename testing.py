import numpy as np
from pprint import pprint as pprint
import datetime
import time


# vector1 = np.arange(50000)
# vector2 = np.arange(50000)
# # matrix1 = np.arange(500000000).reshape(500,1000000)
#
# # pprint(vector1)
# # print(matrix1)
#
# # start = datetime.datetime.now()
# # # print(np.dot(vector1*matrix1))
# # # print(end - start)
#
#
#
# check = int(round(time.time() * 1000))
#
# # print(np.array([np.dot(row,vector1) for row in matrix1]))
# # check2 = int(round(time.time() * 1000))
# # print(check2 - check)
# #
# # print(np.dot(matrix1,vector1))
# # check3 = int(round(time.time() * 1000))
# # print(check3 - check2)
#
#
# # print(np.sum(matrix1*vector1,axis=1))
# # check4 = int(round(time.time() * 1000))
# # print(check4 - check3)
#
# print(np.sum(vector1,vector2))
# check2 = int(round(time.time() * 1000))
# print(check2 - check)
#
# # print(np.dot(vector1,vector2))
# # check2 = int(round(time.time() * 1000))
# # print(check2 - check)
#
# # print(np.array([v1*v2 for v1,v2 in zip(vector1,vector2)]).sum())
# # check3 = int(round(time.time() * 1000))
# # print(check3 - check2)



# import torch
# from torch.autograd import Variable
# import numpy as np
#
# # xy = np.loadtxt('./data/diabetes.csv.gz', delimiter=',', dtype=np.float32)
# # print(xy[:, 0:-1])
#
# # two_d_arr = np.array([[10,20,30],
# #                       [40,50,60],
# #                       [70,80,90]])
# #
# # print(two_d_arr[0][0])
# # print(two_d_arr[1,:3])
#
# new_arr = np.arange(6,15)
# new_arr = new_arr.reshape(3,3)
# print(new_arr > 10)
# print(new_arr[new_arr>10]/1.0)


# # Python program to illustrate
# # enumerate function in loops
# l1 = ["eat", "sleep", "repeat"]
#
# # printing the tuples in object directly
# for ele in enumerate(l1,0):
#     print(ele)
#
# # changing index and printing separately
# for count, ele in enumerate(l1, 100):
#     print(count, ele)
#
# testing = np.loadtxt('./data/diabetes.csv',
#                         delimiter=',', dtype=np.float32)
#
# print(testing)

# import torch
#
# print(torch.cuda.current_device())
#
# print(torch.cuda.device(0))
#
# print(torch.cuda.device_count())
#
# print(torch.cuda.get_device_name(0))


# import torch.cuda
# if torch.cuda.is_available():
#     print('PyTorch found cuda')
# else:
#     print('PyTorch could not find cuda')
#
# import pycuda
# from pycuda import compiler
# import pycuda.driver as drv
#
# drv.init()
# print("%d device(s) found." % drv.Device.count())
#
# for ordinal in range(drv.Device.count()):
#     dev = drv.Device(ordinal)
#     print(ordinal, dev.name())


from pycuda import gpuarray
from pycuda.curandom import rand as curand
 # -- initialize the device
import pycuda.autoinit

height = 100
width = 200
X = curand((height, width), np.float32)
X.flags.c_contiguous
print (type(X))