def linear_search_iterative(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)


if __name__ == "__main__":
    data = [24, 10, 56, 89, 12, 45]
    key = 89

    iter_idx = linear_search_iterative(data, key)
    rec_idx = linear_search_recursive(data, key)

    print(f"Iterative: Element {key} found at index {iter_idx}" if iter_idx != -1 else "Not found")
    print(f"Recursive: Element {key} found at index {rec_idx}" if rec_idx != -1 else "Not found")