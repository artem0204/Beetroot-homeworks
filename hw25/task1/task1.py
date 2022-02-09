def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid - 1)
    # elem > arr[mid]
    return binary_search_recursive(arr, elem, mid + 1, end)


if __name__ == "__main__":
    print(binary_search_recursive([10,20,30,40,50],40))
    
