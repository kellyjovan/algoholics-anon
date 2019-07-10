def heapify(heap, size, indx):
    left_indx = (indx + 1) * 2 - 1
    right_indx = (indx + 1) * 2

    cand = indx

    if left_indx < size and heap[left_indx] > heap[cand]:
        cand = left_indx

    if right_indx < size and heap[right_indx] > heap[cand]:
        cand = right_indx

    if cand != indx:
        heap[indx], heap[cand] = heap[cand], heap[indx]
        heapify(heap, size, cand)

def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [ 12, 11, 13, 5, 6, 7] 
heap_sort(arr)
print(arr)

arr2 = [10, 20, 15, 30, 40]
heap_sort(arr2)
print(arr2)