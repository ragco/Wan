def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Input
# num_elements = int(input("Enter number of elements: "))
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Sort
selection_sort(numbers)

# Output
print("Sorted list:", numbers)