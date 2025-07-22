import matplotlib.pyplot as plt

import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
