import matplotlib.pyplot as plt

categories = ['Apple', 'Banana', 'Cherry']
values = [10, 24, 36]

plt.bar(categories, values, color='skyblue')
plt.title('Fruit Count')
plt.xlabel('Fruits')
plt.ylabel('Count')
plt.show()
