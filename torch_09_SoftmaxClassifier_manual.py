import numpy as np

Y = np.array([1,0,0])

Y_pred1 = np.array([0.7,0.2,0.1])
Y_pred2 = np.array([0.1,0.3,0.6])

loss1 = np.sum(-Y * np.log(Y_pred1))
loss2 = np.sum(-Y * np.log(Y_pred2))

print('loss1 = {}'.format(loss1))
print(np.log(Y_pred1))
print('loss2 = {}'.format(loss2))
print(np.log(Y_pred2))
