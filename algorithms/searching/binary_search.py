def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)


if __name__ == "__main__":
    sorted_data = [5, 12, 19, 27, 34, 48, 63, 75]
    key = 48
    print("Iterative index:", binary_search_iterative(sorted_data, key))
    print("Recursive index:", binary_search_recursive(sorted_data, 0, len(sorted_data) - 1, key))