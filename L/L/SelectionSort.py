def Selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        (arr[i], arr[min]) = (arr[min], arr[i])

arr = []
n = int(input("Enter the number of elements in the array: "))
print("Enter the elements in the array:")
for i in range(0, n):
    l = int(input())
    arr.append(l)

Selectionsort(arr)
print("The array after sorting is:")
print(arr)
