import numpy as np

#arr1 = np.array([1, 2, 3])
#arr2 = np.array([[4, 5, 6],
#                 [7, 8, 9]])
#result = np.vstack((arr1, arr2))
#print(result)


#arr = np.array([[1, 2, 3],
#                [4, 5, 6]])
#flat_arr = arr.flatten()
#print(flat_arr)


#arr = np.array([10, 20, 30, 40, 50])
#reversed_arr = arr[::-1]
#print(reversed_arr)


#arr = np.array([12, 45, 23, 89, 10])
#print("Maximum Value:", np.max(arr))


#arr = np.array([12, 45, 23, 89, 10])
#print("Minimum Value:", np.min(arr))


#arr = np.array([[1, 2, 3],
#                [4, 5, 6]])
#rows, cols = arr.shape
#print("Rows:", rows)
#print("Columns:", cols)


#arr = np.array([[10, 20, 30],
#                [40, 50, 60]])
#print("All Elements:")
#print(arr)
#print("Specific Element:", arr[1, 2])


#arr = np.array([[1, 2, 3],
#                [4, 5, 6]])
#total = 0
#for row in arr:
#    for value in row:
#        total += value
#print("Sum =", total)


#a = np.array([1, 2, 3])
#b = np.array([4, 5, 6])
#print(a + b)


#a = np.array([10, 20, 30])
#b = np.array([1, 2, 3])
#print(a - b)


#a = np.array([1, 2, 3])
#b = np.array([4, 5, 6])
#print(a * b)


#a = np.array([10, 20, 30])
#b = np.array([2, 4, 5])
#print(a / b)


#arr = np.array([
#    [[1, 2], [3, 4]],
#    [[5, 6], [7, 8]]
#])
#for matrix in arr:
#    for row in matrix:
#        for value in row:
#            print(value)


#arr = np.array([
#    [[1, 2], [3, 4]],
#    [[5, 6], [7, 8]]
#])
#for value in np.nditer(arr):
#    print(value)



arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[6, 5, 4],
                 [3, 2, 1]])

combined = np.concatenate((arr1.flatten(), arr2.flatten()))

average = np.average(combined)
mean = np.mean(combined)
median = np.median(combined)

unique_values, counts = np.unique(combined, return_counts=True)
mode = unique_values[np.argmax(counts)]

print("Average =", average)
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)