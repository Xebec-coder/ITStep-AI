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

# У масиві з попереднього завдання створіть маску для
# парних чисел. З її допомогою
# ● виведіть самі числа
# ● замініть їх на 100

mask = (nums % 2 == 0)

print(nums[mask])

nums[mask] = 100

print(nums)

# Створіть 2 масиви типу uint8:
# Масив 1: 128 200 10
# Масив 2: 250 10 34
# Об’єднайте їх у пропорції 20% першого масив + 80%
# другого масиву. В результаті має бути тип даних uint8 та
# числа в діапазоні 0-255

nums_1 = np.array([128, 200, 10])
nums_2 = np.array([250, 10, 34])

nums_1 = nums_1 * 0.2
nums_2 = nums_2 * 0.8

print(nums_1)
print(nums_2)

nums = nums_1 + nums_2
nums = nums.astype(np.uint8)

print(nums)