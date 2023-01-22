def binaryinsertionSort(array, *args):
    for i in range(1, len(array)):
        val = array[i]
        j = binary_search(array, val, 0, i - 1, i)
        yield array, 0, i-1, j, i
        array[:] = array[:j] + [val] + array[j:i] + array[i + 1:]


def binary_search(arr, val, start, end, current):
    if start == end:
        return start if arr[start] > val else start + 1
    if start > end:
        return start

    mid = round((start + end) / 2)
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end, current)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1, current)
    else:
        return mid
