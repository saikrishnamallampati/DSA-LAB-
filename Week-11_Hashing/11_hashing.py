"""Week 11: Hashing - Separate Chaining, Linear Probing and Quadratic Probing."""

EMPTY, DELETED = None, "<deleted>"


class ChainingHashTable:
    """Separate chaining: each slot holds a list (chain) of keys."""

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        chain = self.table[self.hash(key)]
        if key in chain:
            print("Key already exists.")
        else:
            chain.append(key)

    def search(self, key):
        """Return the slot index if the key is present, else -1."""
        idx = self.hash(key)
        return idx if key in self.table[idx] else -1

    def delete(self, key):
        chain = self.table[self.hash(key)]
        if key in chain:
            chain.remove(key)
        else:
            print("Key not found.")

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"{i}: " + (" -> ".join(map(str, chain)) if chain else "empty"))


class OpenAddressingHashTable:
    """Open addressing with linear or quadratic probing."""

    def __init__(self, size, mode):
        self.size = size
        self.mode = mode  # "linear" or "quadratic"
        self.table = [EMPTY] * size

    def hash(self, key):
        return key % self.size

    def probe(self, key, i):
        if self.mode == "linear":
            return (self.hash(key) + i) % self.size
        return (self.hash(key) + i * i) % self.size

    def insert(self, key):
        first_free = None
        for i in range(self.size):
            idx = self.probe(key, i)
            if self.table[idx] == key:
                print("Key already exists.")
                return
            if self.table[idx] in (EMPTY, DELETED):
                if first_free is None:
                    first_free = idx
                if self.table[idx] is EMPTY:
                    break
        if first_free is None:
            print("Hash table is full / no free slot found (probe sequence exhausted).")
        else:
            self.table[first_free] = key

    def search(self, key):
        for i in range(self.size):
            idx = self.probe(key, i)
            if self.table[idx] is EMPTY:
                return -1
            if self.table[idx] == key:
                return idx
        return -1

    def delete(self, key):
        idx = self.search(key)
        if idx == -1:
            print("Key not found.")
        else:
            self.table[idx] = DELETED

    def display(self):
        for i, v in enumerate(self.table):
            print(f"{i}: {'empty' if v is EMPTY else v}")


def main():
    size = int(input("Enter hash table size: "))
    print("\nChoose technique:\n1. Separate Chaining\n2. Linear Probing\n3. Quadratic Probing")
    tech = int(input("Enter your choice: "))
    if tech == 1:
        ht = ChainingHashTable(size)
    elif tech == 2:
        ht = OpenAddressingHashTable(size, "linear")
    elif tech == 3:
        ht = OpenAddressingHashTable(size, "quadratic")
    else:
        print("Invalid technique.")
        return

    while True:
        print("\n1. Insert  2. Search  3. Delete  4. Display  5. Exit")
        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue
        if ch == 1:
            ht.insert(int(input("Enter key: ")))
        elif ch == 2:
            r = ht.search(int(input("Enter key to search: ")))
            print(f"Found at slot {r}." if r != -1 else "Not found.")
        elif ch == 3:
            ht.delete(int(input("Enter key to delete: ")))
        elif ch == 4:
            ht.display()
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
