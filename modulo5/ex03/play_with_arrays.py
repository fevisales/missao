#!/usr/bin/env python3

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = []

for num in arr1:
    if num > 5:
        arr2.append(num + 2)
print(arr1)
print(set(arr2))
