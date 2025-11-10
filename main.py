import numpy as np
# #
# # array = np.array([1, 2, 3, 4, 5])
# #
# # print(array)
# # print(array.shape)
# # print(array.dtype)
#
# # nums = np.arange(10, 20, 2) # масив діапазоном, ранге
# #
# # print(nums)
# #
# # nums = np.zeros(shape=(3, 4))
# # print(nums)
# #
# # nums = np.arange(10, 20)
# # new_nums = nums.reshape((2, 5))
# # print(new_nums)
# # print(new_nums.shape)
#
# # index
#
# nums = np.arange(10, 20)
#
# print(nums)
# # print(nums[2])
# # print(nums[2:5])
# # print(nums[2:7:2])
# # print(nums[:3])
# # print(nums[-3:])
# # print(nums[:-3])
# num = 2
#
# nums[2] = 0
# nums[num:7] *= -1
#
# print(nums)
# Використовуючи індекси виведіть:
# ● число 7
# ● другий рядок
# ● останній стовпчик
# ● праву половину
# ● жовту область
# ● замініть жовту область на -1
# ● зробіть перший стовпчик таким самим як і другий
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
nums = np.arange(1, 13)
nums = nums.reshape(3, 4)

print(nums)
print(nums[1, 2])
print(nums[1])
print(nums[:, -1])
print(nums[:, -2:])
print(nums[1:3, 1:3])
nums[1:3, 1:3] = -1
print(nums)
nums[:, 0] = nums[:, 1]
print(nums)
print()

# У масиві з попереднього завдання створіть маску для
# чисел які більші за 6. З її допомогою
# ● виведіть кількість чисел більших за 6
# ● виведіть самі числа
# ● до кожного числа яке відповідає масці додайте 10
# ● кожне число що не відповідає масці помножте на -1
# ● замініть ці числа які відповідають масці на відповідні
# їм з масиву
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0

mask = nums > 6
print(mask)
print(nums[mask])

print(np.sum(mask))

nums[mask] += 10
print(nums)

nums[~mask] *= -1
print(nums)

array = np.array([[ 1, 0, 1, 0],
[0, 1, 0, 1],
[1, 0, 1, 0]])
print(mask)
print(array)
nums[~mask] = array[~mask]

print()
print(nums)
print()
