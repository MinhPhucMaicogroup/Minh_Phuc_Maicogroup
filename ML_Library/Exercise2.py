import numpy as np
import matplotlib.pyplot as plt

# A)
plt.figure(1)
plt.title("ABC")
x_axis = np.arange(1, 5)
y_axis = np.array([1, 4, 3, 9])
x_point = np.array([1, 2, 3, 4, 5])
y_point = np.array([1, 6, 2, 3, 9])
plt.xlabel("Hoanh do")
plt.ylabel("Tung do")
plt.plot(x_axis, y_axis, "r")
plt.scatter(x_point, y_point, c="g", marker="^")

# B)
plt.figure(2)
plt.title("Bar chart")
y_axis1 = np.array([50, 100, 200, 10])
y_axis2 = np.array([85, 25, 20, 40])
index = np.arange(1, 5)
barwidth = 0.1
plt.xticks(x_axis)
plt.yticks(np.arange(0, 225, step=25))
plt.bar(index-barwidth, y_axis1, color='g', width=barwidth*2, label="Green")
plt.bar(index+barwidth, y_axis2, color='#e2eb34', width=barwidth*2, label="Yellow")
plt.legend()

# C)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("abc")

ax1.set_title("abc1")
x_axis1 = np.arange(1, 5)
y_axis1 = np.array([1, 3.5, 2.5, 8.5])
ax1.set_yticks(np.arange(2.5, 10.0, step=2.5))
ax1.plot(x_axis1, y_axis1, color='g')

ax2.set_title("abc2")
x_axis2 = np.arange(1, 6)
y_axis2 = np.array([1, 5.5, 2.5, 3, 8])
ax2.set_yticks(np.arange(2.5, 10.0, step=2.5))
ax2.plot(x_axis2, y_axis2, color='r')

ax3.set_title("abc3")
ax3.set_xticks(np.arange(0.0, 1.2, step=0.2))
ax3.set_yticks(np.arange(0.0, 1.25, step=0.25))

ax4.set_title("abc4")
x_axis4 = np.array([1, 2, 4])
y_axis4 = np.array([0.7, 5, 0.7])
ax4.set_yticks(np.arange(2, 6, step=2))
ax4.plot(x_axis4, y_axis4, color='y')

plt.show()


