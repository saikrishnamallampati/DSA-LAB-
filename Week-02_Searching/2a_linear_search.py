"""Week 2 (A): Linear Search."""


def linear_search(arr, key):
    for i, value in enumerate(arr):
        if value == key:
            return i
    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter elements separated by spaces: ").split()))
    key = int(input("Enter element to search: "))
    pos = linear_search(arr, key)
    if pos == -1:
        print("Element not found.")
    else:
        print(f"Element found at index {pos}.")
