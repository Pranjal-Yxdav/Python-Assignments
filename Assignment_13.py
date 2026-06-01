import numpy as np
import matplotlib.pyplot as plt

#1
#arr = np.array([[6, -8, 73, -110],
#                [np.nan, -8, 0, 94]])
#arr = np.nan_to_num(arr, nan=0)
#print(arr)
#print(arr.T)


# 2
#arr = np.arange(24).reshape(2, 3, 4)
#new_arr = np.moveaxis(arr, 0, 2)
#print(new_arr.shape)
#print(new_arr)

# 3
#arr = np.array([[10, np.nan, 30],
#                [40, 50, np.nan],
#                [70, 80, 90]])
#col_mean = np.nanmean(arr, axis=0)
#for i in range(arr.shape[1]):
#    arr[np.isnan(arr[:, i]), i] = col_mean[i]
#print(arr)

# 4
#arr = np.array([[-5, 10, -8],
#                [15, -2, 20]])
#arr[arr < 0] = 0
#print(arr)


# 5
#arr1 = np.array([[10, 20],
#                 [30, 40]])
#arr2 = np.array([[15, 25],
#                 [35, 45]])
#combined = np.concatenate((arr1, arr2))
#print("Mean:", np.mean(combined))
#print("Median:", np.median(combined))
#values, counts = np.unique(combined, return_counts=True)
#mode = values[np.argmax(counts)]
#print("Mode:", mode)

# 6
#A = np.array([[1, -2, 3],
#              [-1, 3, -1],
#              [2, -5, 5]])
#B = np.array([9, -6, 17])
#A_inv = np.linalg.inv(A)
#solution = np.dot(A_inv, B)
#print("x =", solution[0])
#print("y =", solution[1])
#print("z =", solution[2])


# 7
subjects = ["Maths", "Python", "Java", "DBMS", "English"]
sem1 = [72, 75, 68, 70, 80]
sem2 = [78, 82, 74, 76, 85]
x = np.arange(len(subjects))
plt.figure(figsize=(8, 5))
plt.plot(x, sem1, marker="o", label="Semester 1")
plt.plot(x, sem2, marker="s", label="Semester 2")
plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.xticks(x, subjects)
plt.legend()
plt.grid(True)
plt.show()