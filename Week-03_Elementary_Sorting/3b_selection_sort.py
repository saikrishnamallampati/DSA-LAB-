"""Week 3 (B): Selection Sort (user input)."""


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    arr = list(map(int, input("Enter elements separated by spaces: ").split()))
    print("Sorted list:", selection_sort(arr))
