import numpy as np

count = 0
for i in range(100):
    num = np.random.rand()
    if num > 0.5:
        count += 1
    print(num)

print(count)