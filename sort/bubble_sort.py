def bubble_sort(array):
    for i in range(1, len(array) - 1):
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] + array[j + 1], array[j]
    return array
