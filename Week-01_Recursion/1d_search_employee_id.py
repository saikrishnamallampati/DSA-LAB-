"""Week 1 (D): Recursive search for an employee ID in a list."""


def search(ids, target, index=0):
    if index == len(ids):
        return -1
    if ids[index] == target:
        return index
    return search(ids, target, index + 1)


if __name__ == "__main__":
    ids = input("Enter employee IDs separated by spaces: ").split()
    target = input("Enter employee ID to search: ")
    pos = search(ids, target)
    if pos == -1:
        print(f"Employee ID {target} not found.")
    else:
        print(f"Employee ID {target} found at position {pos}.")
