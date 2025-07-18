import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, label='Line')      # Line chart
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Basic Line Plot')
plt.legend()
plt.grid(True)
plt.show()
