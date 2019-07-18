def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = int(n/2)
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(arr_1, arr_2):
    output = []

    i, j = 0, 0

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            output.append(arr_1[i])
            i += 1
        else:
            output.append(arr_2[j])
            j += 1

    output.extend(arr_1[i:])
    output.extend(arr_2[j:])

    return output


arr1 = [1, 5, 7, 8, 10]
arr2 = [2, 3, 4, 9, 11, 15]

print(merge_sort([1, 4, 2, 5, 3, 3, 9, 11, 6]))