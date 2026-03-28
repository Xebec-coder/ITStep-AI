import numpy as np
from numpy.ma.core import reshape

# new_array = np.arange(1, 11)
#
# print(new_array)
# print(new_array.shape)
# print(new_array.dtype)
#
# nums = new_array.reshape(5, 2)
#
# print(nums)
# print(nums)
# print(nums)
nums = np.arange(1, 17)
nums = nums.reshape(4, 4)

print(nums)
# Використовуючи індекси виведіть:
# ● число 14
# ● третій рядок
# ● перший стовпчик
# ● верхню половину
# ● замініть числа в рядках 2-3 на 100
# ● зробіть другий рядок таким як останній рядок
print(nums[3, 1])
print(nums[2])
print(nums[:4, 0])

nums[1:3, ] = 100

print(nums)

nums[1, ] = nums[3,]

print(nums)