import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0  # a random guess: random value

# our model forward pass


def forward(x):
    return x * w


# Loss function
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)


w_list = []
mse_list = []
for w in np.arange(0.0,4.1,0.1):
    print('w = ', w)
    l_sum = 0
    for x_val, y_val in zip(x_data, y_data):
        y_pred_val = forward(x_val)
        l = loss(x_val, y_val)
        l_sum += l
        print("\t", x_val, y_val, y_pred_val, l)
    print("MSE = ", l_sum/3)
    w_list.append(w)
    mse_list.append(l_sum/3)
print(w_list)
print(mse_list)

plt.plot(w_list, mse_list)
plt.ylabel('Loss')
plt.xlabel('w')
plt.show()









# # compute gradient
# def gradient(x, y):  # d_loss/d_w
#     return 2 * x * (x * w - y)
#
# # Before training
# print("predict (before training)",  4, forward(4))
#
# # Training loop
# for epoch in range(100):
#     for x_val, y_val in zip(x_data, y_data):
#         grad = gradient(x_val, y_val)

#         print("\tgrad: ", x_val, y_val, round(grad, 2))
#         l = loss(x_val, y_val)
#
#     print("progress:", epoch, "w=", round(w, 2), "loss=", round(l, 2))
#
# # After training
# print("predict (after training)",  "4 hours", forward(4))
# print(list(zip(x_data, y_data)))