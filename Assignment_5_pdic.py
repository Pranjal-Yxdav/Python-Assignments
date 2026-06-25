# 1
print("1")

t = (1, 2, 3)
print("Original Tuple:", t)
print("Repeated Tuple:", t * 3)

print()

# 2
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

new_tuple = t1 + t2 + t3

print("Joined Tuple:", new_tuple)

print()

# 3
numbers = (10, 20, 30, 40, 50)

element = 30

if element in numbers:
    print(element, "exists in tuple.")
else:
    print(element, "does not exist.")

print()

# 4
nums = (12, 5, 18, 7, 25)

total = 0
highest = nums[0]
lowest = nums[0]

for i in nums:
    total += i

    if i > highest:
        highest = i

    if i < lowest:
        lowest = i

print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)

print()

# 5
n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = ()

for i in n:
    if i > 10:
        filtered += (i,)

print("Filtered Tuple:", filtered)

print()

# 6
s = {"cat", "dog", "bird", "fish"}

count = 0

for item in s:
    count += 1

print("Number of elements:", count)

print()

# 7
set1 = {1, 2, 3}
set2 = {3, 4, 5}

combined = set1 | set2

print("Combined Set:", combined)

print()

# 8
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

common = s1 & s2

print("Common Elements:", common)

print()

# 9
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result = s1 ^ s2

print("Symmetric Difference:", result)

print()