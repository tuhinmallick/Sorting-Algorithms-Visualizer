def get_gap(prev_gap) -> int:
    gap = int(prev_gap/1.3)
    return max(gap, 1)
    

def combSort(array, *args):
    size = len(array)
    gap = size
    swapped = True

    while gap != 1 or swapped:
        gap = get_gap(gap)
        swapped = False

        for idx in range(size - gap):
            yield array, idx, idx+gap, -1, -1
            if array[idx] > array[idx + gap]:
                array[idx], array[idx + gap] = array[idx + gap], array[idx]
                swapped = True
