import numpy as np

# 1
arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = arr1d.reshape(2, 3)

print(arr1d)
print(arr2d)

# 2
print("Shape:", arr2d.shape)
print("Dimensions:", arr2d.ndim)
print("Data Type:", arr2d.dtype)
print("Item Size:", arr2d.itemsize)

# 3
arr = np.full((3, 3), 9)
print(arr)

# 4
arr = np.linspace(25, 125, 10)
print(arr)

# 5
lst = [10, 20, 30, 40, 50]
arr = np.array(lst)
print(arr)

# 6
arr = np.array([1, 2, 3, 4, 5])
print(arr[::-1])

# 7
arr = np.arange(48).reshape(4, 4, 3)
print(arr[1, 0, 2])

# 8
arr = np.arange(1, 17).reshape(4, 4)
print(arr[0::2, 1::2])

# 9
arr = np.arange(48).reshape(4, 4, 3)
print(arr[1, :2, :2])

# 10
arr = np.array([[23, 56, 78, 93],
                [71, 82, 13, 24]])

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i, j] % 2 != 0:
            arr[i, j] = -1

print(arr)

# 11
arr = np.array([1, 0, 2, 0, 3, 0, 4])
print(np.nonzero(arr))

# 12
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

print(arr1 + arr2)
print(arr1 * arr2)

# 13
arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])

print(np.dot(arr1, arr2))