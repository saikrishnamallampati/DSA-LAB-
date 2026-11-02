"""Week 2 (B): Binary Search (verified with sorted and unsorted lists).

Binary search only works correctly on a SORTED list, so the program first
checks whether the input is sorted and shows what happens when it is not.
"""


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter elements separated by spaces: ").split()))
    key = int(input("Enter element to search: "))

    if is_sorted(arr):
        print("List is sorted.")
    else:
        print("List is NOT sorted - binary search may give a wrong result.")
        print("Result on the unsorted list:", binary_search(arr, key))
        arr.sort()
        print("Sorted list:", arr)

    pos = binary_search(arr, key)
    if pos == -1:
        print("Element not found.")
    else:
        print(f"Element found at index {pos} (in the sorted list).")
