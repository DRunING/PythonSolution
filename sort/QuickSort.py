def quick_sort(arr, i, j):
    if i < j:
        l = i
        r = j
        x = arr[l]
        while l < r:
            while l < r and x < arr[r]:
                r -= 1
            if l < r:
                arr[l] = arr[r]
                l += 1
            while l < r and arr[l] < x:
                l += 1
            if l < r:
                arr[r] = arr[l]
                r -= 1
        arr[l] = x
        quick_sort(arr, i, l - 1)
        quick_sort(arr, l + 1, j)


if __name__ == "__main__":
    arr = [11, 2, 3, 0, 1, 10, 12, 9, 6]
    quick_sort(arr, 0, 8)
    print arr