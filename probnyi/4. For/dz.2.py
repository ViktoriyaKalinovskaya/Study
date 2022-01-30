arr = [1, 8, 2, 4, 3, 6, 8, 4, 8, 9, 45, 30, 12, 4, 0, 45, 45]
arr1 = []
for i in arr:
    if arr.count(i) > 2 and i not in arr1:
        arr1.append(i)
print(arr1)
