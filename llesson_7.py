import random

array_length = 10  
random_array = [random.randint(1, 100) for i in range(array_length)]

print("Исходный массив:", random_array)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


bubble_sorted_array = random_array.copy()
selection_sorted_array = random_array.copy()
insertion_sorted_array = random_array.copy()
merge_sorted_array = random_array.copy()

bubble_sort(bubble_sorted_array)
selection_sort(selection_sorted_array)
insertion_sort(insertion_sorted_array)
merge_sort(merge_sorted_array)

print("Отсортированный массив (пузырьком):", bubble_sorted_array)
print("Отсортированный массив (выбором):", selection_sorted_array)
print("Отсортированный массив (вставками):", insertion_sorted_array)
print("Отсортированный массив (слиянием):", merge_sorted_array)
