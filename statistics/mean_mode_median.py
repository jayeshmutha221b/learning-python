import numpy as np
from statistics import mode 

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [1, 5, 4, 2, 76, 3, 9]
z = [1, 1, 1,3, 2, 2, 3, 3, 4, 5, 4, 3, 5, 6, 7, 7, 8, 9, 9]


x1 = np.array(x)
y1 = np.array(y)

print('Mean of x=', x1.mean())
print('Median of y=', np.median(y1))
# Z fails if two nodes found
print(mode(z))
