import numpy as np

# 1
arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

arr = np.nan_to_num(arr, nan =0)

print("After Replacing NaN with 0:")
print(arr)

print("\nAfter Interchanging Rows and Columns:")
print(arr.T)

# 2
arr = np.arange(24).reshape(2, 3, 4)

print("Original Shape:", arr.shape)

new_arr = np.moveaxis(arr, 0, 2)

print("New Shape:", new_arr.shape)
print(new_arr)


# 3
arr = np.array([[1, 2, np.nan],
                [4, np.nan, 6],
                [7, 8, 9]])

col_mean = np.nanmean(arr, axis=0)

inds = np.where(np.isnan(arr))

arr[inds] = np.take(col_mean, inds[1])

print(arr)

# 4
arr = np.array([6, -8, 73, -110, 25, -5])
arr = np.where(arr < 0, 0, arr)
print(arr)
