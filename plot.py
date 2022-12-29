import matplotlib.pyplot as plt


client_1_train_acc = [0.666, 0.819, 0.921, 0.970, 0.991, 0.958, 0.989, 0.996, 0.997, 0.997]
client_1_train_acc = [i * 100 for i in client_1_train_acc]
client_1_train_loss = [0.311, 0.169, 0.105, 0.069, 0.046, 0.076, 0.047, 0.029, 0.018, 0.015]
client_1_train_loss = [i * 100 for i in client_1_train_loss]
client_1_val_acc = [0.811, 0.888, 0.944, 0.972, 0.979, 0.986, 0.986, 0.986, 0.979, 0.986]
client_1_val_acc = [i * 100 for i in client_1_val_acc]
client_1_val_loss = [0.197, 0.112, 0.086, 0.056, 0.044, 0.052, 0.041, 0.028, 0.036, 0.020]
client_1_val_loss = [i * 100 for i in client_1_val_loss]

client_2_train_acc = [0.672, 0.780, 0.869, 0.926, 0.961, 0.965, 0.991, 0.996, 0.999, 0.999]
client_2_train_acc = [i * 100 for i in client_2_train_acc]
client_2_train_loss = [0.339, 0.238, 0.133, 0.088, 0.065, 0.066, 0.037, 0.026, 0.016, 0.011]
client_2_train_loss = [i * 100 for i in client_2_train_loss]
client_2_val_acc = [0.748, 0.797, 0.818, 0.895, 0.930, 0.902, 0.979, 0.965, 0.979, 0.944]
client_2_val_acc = [i * 100 for i in client_2_val_acc]
client_2_val_loss = [0.308, 0.191, 0.140, 0.107, 0.085, 0.150, 0.051, 0.043, 0.039, 0.042]
client_2_val_loss = [i * 100 for i in client_2_val_loss]

client_3_train_acc = [0.662, 0.756, 0.820, 0.919, 0.961, 0.964, 0.990, 0.998, 1.000, 1.000]
client_3_train_acc = [i * 100 for i in client_3_train_acc]
client_3_train_loss = [0.342, 0.275, 0.166, 0.099, 0.071, 0.071, 0.040, 0.024, 0.014, 0.010]
client_3_train_loss = [i * 100 for i in client_3_train_loss]
client_3_val_acc = [0.748, 0.769, 0.860, 0.930, 0.958, 0.986, 0.993, 0.993, 0.993, 0.993]
client_3_val_acc = [i * 100 for i in client_3_val_acc]
client_3_val_loss = [0.322, 0.232, 0.117, 0.094, 0.082, 0.049, 0.047, 0.027, 0.016, 0.014]
client_3_val_loss = [i * 100 for i in client_3_val_loss]

client_4_train_acc = [0.651, 0.755, 0.826, 0.920, 0.965, 0.963, 0.979, 0.999, 0.998, 1.000]
client_4_train_acc = [i * 100 for i in client_4_train_acc]
client_4_train_loss = [0.336, 0.265, 0.170, 0.103, 0.070, 0.073, 0.046, 0.025, 0.016, 0.010]
client_4_train_loss = [i * 100 for i in client_4_train_loss]
client_4_val_acc = [0.708, 0.806, 0.847, 0.910, 0.979, 0.979, 0.993, 0.993, 0.993, 0.979]
client_4_val_acc = [i * 100 for i in client_4_val_acc]
client_4_val_loss = [0.308, 0.209, 0.121, 0.094, 0.072, 0.045, 0.029, 0.024, 0.018, 0.023]
client_4_val_loss = [i * 100 for i in client_4_val_loss]

x = range(1, 11)

fig, axs = plt.subplots(4, 4)

axs[0, 0].plot(x[:5], client_1_train_acc[:5], c='b')
axs[0, 0].plot(x[5:], client_1_train_acc[5:], c='r')
axs[0, 0].scatter(x[:5], client_1_train_acc[:5], c='b')
axs[0, 0].scatter(x[5:], client_1_train_acc[5:], c='r')
axs[0, 0].set_title('Client 1')
axs[0, 0].set(ylabel='Train Accuracy')
axs[0, 0].grid()

axs[0, 1].plot(x[:5], client_2_train_acc[:5], c='b')
axs[0, 1].plot(x[5:], client_2_train_acc[5:], c='r')
axs[0, 1].scatter(x[:5], client_2_train_acc[:5], c='b')
axs[0, 1].scatter(x[5:], client_2_train_acc[5:], c='r')
axs[0, 1].set_title('Client 2')
axs[0, 1].grid()

axs[0, 2].plot(x[:5], client_3_train_acc[:5], c='b')
axs[0, 2].plot(x[5:], client_3_train_acc[5:], c='r')
axs[0, 2].scatter(x[:5], client_3_train_acc[:5], c='b')
axs[0, 2].scatter(x[5:], client_3_train_acc[5:], c='r')
axs[0, 2].set_title('Client 3')
axs[0, 2].grid()

axs[0, 3].plot(x[:5], client_4_train_acc[:5], c='b')
axs[0, 3].plot(x[5:], client_4_train_acc[5:], c='r')
axs[0, 3].scatter(x[:5], client_4_train_acc[:5], c='b')
axs[0, 3].scatter(x[5:], client_4_train_acc[5:], c='r')
axs[0, 3].set_title('Client 4')
axs[0, 3].grid()

axs[1, 0].plot(x[:5], client_1_train_loss[:5], c='b')
axs[1, 0].plot(x[5:], client_1_train_loss[5:], c='r')
axs[1, 0].scatter(x[:5], client_1_train_loss[:5], c='b')
axs[1, 0].scatter(x[5:], client_1_train_loss[5:], c='r')
axs[1, 0].set(ylabel='Train Loss')
axs[1, 0].grid()

axs[1, 1].plot(x[:5], client_2_train_loss[:5], c='b')
axs[1, 1].plot(x[5:], client_2_train_loss[5:], c='r')
axs[1, 1].scatter(x[:5], client_2_train_loss[:5], c='b')
axs[1, 1].scatter(x[5:], client_2_train_loss[5:], c='r')
axs[1, 1].grid()

axs[1, 2].plot(x[:5], client_3_train_loss[:5], c='b')
axs[1, 2].plot(x[5:], client_3_train_loss[5:], c='r')
axs[1, 2].scatter(x[:5], client_3_train_loss[:5], c='b')
axs[1, 2].scatter(x[5:], client_3_train_loss[5:], c='r')
axs[1, 2].grid()

axs[1, 3].plot(x[:5], client_3_train_loss[:5], c='b')
axs[1, 3].plot(x[5:], client_3_train_loss[5:], c='r')
axs[1, 3].scatter(x[:5], client_3_train_loss[:5], c='b')
axs[1, 3].scatter(x[5:], client_3_train_loss[5:], c='r')
axs[1, 3].grid()

axs[2, 0].plot(x[:5], client_1_val_acc[:5], c='b')
axs[2, 0].plot(x[5:], client_1_val_acc[5:], c='r')
axs[2, 0].scatter(x[:5], client_1_val_acc[:5], c='b')
axs[2, 0].scatter(x[5:], client_1_val_acc[5:], c='r')
axs[2, 0].set(ylabel='Val Accuracy')
axs[2, 0].grid()

axs[2, 1].plot(x[:5], client_2_val_acc[:5], c='b')
axs[2, 1].plot(x[5:], client_2_val_acc[5:], c='r')
axs[2, 1].scatter(x[:5], client_2_val_acc[:5], c='b')
axs[2, 1].scatter(x[5:], client_2_val_acc[5:], c='r')
axs[2, 1].grid()

axs[2, 2].plot(x[:5], client_3_val_acc[:5], c='b')
axs[2, 2].plot(x[5:], client_3_val_acc[5:], c='r')
axs[2, 2].scatter(x[:5], client_3_val_acc[:5], c='b')
axs[2, 2].scatter(x[5:], client_3_val_acc[5:], c='r')
axs[2, 2].grid()

axs[2, 3].plot(x[:5], client_4_val_acc[:5], c='b')
axs[2, 3].plot(x[5:], client_4_val_acc[5:], c='r')
axs[2, 3].scatter(x[:5], client_4_val_acc[:5], c='b')
axs[2, 3].scatter(x[5:], client_4_val_acc[5:], c='r')
axs[2, 3].grid()

axs[3, 0].plot(x[:5], client_1_val_loss[:5], c='b')
axs[3, 0].plot(x[5:], client_1_val_loss[5:], c='r')
axs[3, 0].scatter(x[:5], client_1_val_loss[:5], c='b')
axs[3, 0].scatter(x[5:], client_1_val_loss[5:], c='r')
axs[3, 0].set(ylabel='Val Loss')
axs[3, 0].grid()

axs[3, 1].plot(x[:5], client_2_val_loss[:5], c='b')
axs[3, 1].plot(x[5:], client_2_val_loss[5:], c='r')
axs[3, 1].scatter(x[:5], client_2_val_loss[:5], c='b')
axs[3, 1].scatter(x[5:], client_2_val_loss[5:], c='r')
axs[3, 1].grid()

axs[3, 2].plot(x[:5], client_3_val_loss[:5], c='b')
axs[3, 2].plot(x[5:], client_3_val_loss[5:], c='r')
axs[3, 2].scatter(x[:5], client_3_val_loss[:5], c='b')
axs[3, 2].scatter(x[5:], client_3_val_loss[5:], c='r')
axs[3, 2].grid()

axs[3, 3].plot(x[:5], client_3_val_loss[:5], c='b')
axs[3, 3].plot(x[5:], client_3_val_loss[5:], c='r')
axs[3, 3].scatter(x[:5], client_3_val_loss[:5], c='b')
axs[3, 3].scatter(x[5:], client_3_val_loss[5:], c='r')
axs[3, 3].legend(['Round 1', 'Round 2'])
axs[3, 3].grid()

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()


plt.show()