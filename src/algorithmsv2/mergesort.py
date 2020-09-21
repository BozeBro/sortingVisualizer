def merge_sort(array, start=None, end=None):
    if end is None or start is None:
        end = len(array) - 1
        start = 0
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(array, start, mid)
    yield from merge_sort(array, mid + 1, end)
    yield from merge(array, start, mid, end)


def merge(array, start, mid, end):
    merged, left, right = [], start, mid + 1

    while left <= mid and right <= end:
        if array[left] < array[right]:
            merged.append((left, array[left]))
            left += 1
        else:
            merged.append((right, array[right]))
            right += 1

    while left <= mid:
        merged.append((left, array[left]))
        left += 1

    while right <= end:
        merged.append((right, array[right]))
        right += 1

    for i, (ind, val) in enumerate(merged):
        array[start + i] = val
        yield start + i, val / len(array)
