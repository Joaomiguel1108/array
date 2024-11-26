import numpy as np



array1 = np.arange(2,21)
nums= []


for num in array1:
    if num %2 == 0:
        nums.append(num)


print(nums)
