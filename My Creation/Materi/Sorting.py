# # PENGURUTAN -SORTING

# # Membuat fungsi yang menrima parameter array
# def selection_sort(array):
#     # membuat for perulangan sebanyak isi/value dari array
#     for i in range(len(array)-1):
#         # membuat variabel index_awal dengan mengisi nya dengan i
#         index_awal = i
#         # membuat perulangan dimana i + 1, dan loop sebanyak isi data array
#         for j in range(i+1, len(array)):
#             # jika array [j] lebih kecil dari array [index_awal]
#             if array[j] < array[index_awal]:
#                 # maka index_awal = j
#                 index_awal = j
#         # mengubah value
#         array[i], array[index_awal] = array[index_awal], array[i]

# angka = [1, 4, 3, 9, 6, 5]
# selection_sort(angka)

# print(angka)



angka = [9, 5, 8, 6, 7, 4, 3, 1, 2]

# SELECTION_SORT
def selection_sort(array):

    for i in range(len(array)-1):
        index_awal = i
        for j in range(i+1, len(array)):
            if array[j] < array[index_awal]:
                index_awal = j
        array[i], array[index_awal] = array[index_awal], array[i]


# BUBBLE_SORT
def bubble_sort(array):
    for i in range (len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


# INSERTION_SORT
def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = value


# MERGE_SORT
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        leftarray = array[:mid]
        rightarray = array[mid:]
        merge_sort(leftarray)
        merge_sort(rightarray)
        merge(leftarray, rightarray, array)


def merge(left, right, array):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        array[k] = left[i]
        k = k + 1
        i = i + 1

    while j < len(right):
        array[k] = right[j]
        k = k + 1
        j = j + 1


# QUICK_SORT
def quick_sort(array):
    quick_sort_rec(array, 0, len(array)-1)

def quick_sort_rec(array, start, end):
    if start < end:
        pivot_idx = partition(array, start, end)
        quick_sort_rec(array, start, pivot_idx - 1)
        quick_sort_rec(array, pivot_idx + 1, end)

def partition(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[i], array[end], = array[end], array[i]
    return i


quick_sort(angka)
print(angka)
