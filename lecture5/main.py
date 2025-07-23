import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]

plt.subplot(1, 2, 1)
plt.plot(x, y1, 'g')
plt.title('Square')

plt.subplot(1, 2, 2)
plt.plot(x, y2, 'b')
plt.title('Cube')

plt.suptitle('Subplot Example')
plt.tight_layout()
plt.show()
