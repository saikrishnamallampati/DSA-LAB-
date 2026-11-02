"""Week 5 (C): Circular Linked List (CLL) with menu-driven operations."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def _last(self):
        cur = self.head
        while cur.next is not self.head:
            cur = cur.next
        return cur

    def _find(self, value):
        if not self.head:
            return None
        cur = self.head
        while True:
            if cur.data == value:
                return cur
            cur = cur.next
            if cur is self.head:
                return None

    def _remove(self, target):
        if self.head is target:
            if target.next is target:
                self.head = None
            else:
                last = self._last()
                self.head = target.next
                last.next = self.head
            return
        cur = self.head
        while cur.next is not target:
            cur = cur.next
        cur.next = target.next

    def create(self, values):
        self.head = None
        for v in values:
            self.insert_end(v)

    def insert_beginning(self, data):
        node = Node(data)
        if not self.head:
            node.next = node
            self.head = node
            return
        last = self._last()
        node.next = self.head
        last.next = node
        self.head = node

    def insert_end(self, data):
        node = Node(data)
        if not self.head:
            node.next = node
            self.head = node
            return
        last = self._last()
        last.next = node
        node.next = self.head

    def insert_at_index(self, index, data):
        if index < 0 or index > self.count():
            print("Invalid index.")
            return
        if index == 0:
            self.insert_beginning(data)
            return
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        node = Node(data)
        node.next = cur.next
        cur.next = node

    def delete_by_value(self, value):
        if not self.head:
            print("List is empty.")
            return
        node = self._find(value)
        if node:
            self._remove(node)
        else:
            print("Value not found.")

    def delete_prior_node(self, value):
        """Delete the node that comes just before the node holding `value`."""
        node = self._find(value)
        if not node:
            print("Value not found.")
            return
        if node.next is node:
            print("Only one node - no prior node to delete.")
            return
        prior = self.head
        while prior.next is not node:
            prior = prior.next
        self._remove(prior)

    def delete_last(self):
        if not self.head:
            print("List is empty.")
            return
        self._remove(self._last())

    def count(self):
        if not self.head:
            return 0
        n, cur = 1, self.head.next
        while cur is not self.head:
            n += 1
            cur = cur.next
        return n

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        items, cur = [str(self.head.data)], self.head.next
        while cur is not self.head:
            items.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(items) + " -> (back to head)")


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid integer.")
        return None


def main():
    ll = CircularLinkedList()
    while True:
        print("\n----- LINKED LIST MENU -----")
        print("1. Create LL")
        print("2. Insert at Beginning")
        print("3. Insert at End")
        print("4. Insert at Index")
        print("5. Delete by Value")
        print("6. Delete Prior Node")
        print("7. Delete Last Node")
        print("8. Count Nodes")
        print("9. Display/Traverse")
        print("10. Exit")
        choice = read_int("Enter your choice: ")
        if choice is None:
            continue

        if choice == 1:
            try:
                values = list(map(int, input("Enter values separated by spaces: ").split()))
            except ValueError:
                print("Please enter integers only.")
                continue
            ll.create(values)
            print("List created.")
        elif choice == 2:
            v = read_int("Enter value: ")
            if v is not None:
                ll.insert_beginning(v)
        elif choice == 3:
            v = read_int("Enter value: ")
            if v is not None:
                ll.insert_end(v)
        elif choice == 4:
            i = read_int("Enter index: ")
            v = read_int("Enter value: ")
            if i is not None and v is not None:
                ll.insert_at_index(i, v)
        elif choice == 5:
            v = read_int("Enter value to delete: ")
            if v is not None:
                ll.delete_by_value(v)
        elif choice == 6:
            v = read_int("Delete the node prior to the node with value: ")
            if v is not None:
                ll.delete_prior_node(v)
        elif choice == 7:
            ll.delete_last()
        elif choice == 8:
            print("Number of nodes:", ll.count())
        elif choice == 9:
            ll.display()
        elif choice == 10:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 10.")


if __name__ == "__main__":
    main()
