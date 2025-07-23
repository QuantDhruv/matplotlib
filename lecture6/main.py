import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.annotate('Highest Point', xy=(5, 25), xytext=(3, 30),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title('Plot with Annotation')
plt.show()
