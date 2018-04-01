def heap_sort(arr):
    for j in range(len(arr)/2 - 1, 0, -1):
        adjust_heap(arr, j, len(arr))
    print arr
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        adjust_heap(arr, 0, i)


def adjust_heap(arr, i, length):
    tmp = arr[i]
    k = 2 * i + 1
    while k < length:
        if k + 1 < length and arr[k + 1] > arr[k]:
            k += 1
        if arr[k] > tmp:
            arr[i] = arr[k]
            i = k
        else:
            break
        k = i * 2 + 1
    arr[i] = tmp


if __name__ == "__main__":
    arr = [11, 2, 3, 0, 1, 10, 12, 9, 6]
    heap_sort(arr)
    print arr