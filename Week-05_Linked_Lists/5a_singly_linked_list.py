"""Week 5 (A): Singly Linked List (SLL) with menu-driven operations."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def create(self, values):
        self.head = None
        for v in values:
            self.insert_end(v)

    def insert_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

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
        if self.head.data == value:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.data != value:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
        else:
            print("Value not found.")

    def delete_prior_node(self, value):
        """Delete the node that comes just before the node holding `value`."""
        if not self.head or self.head.data == value:
            print("No prior node exists.")
            return
        if self.head.next and self.head.next.data == value:
            self.head = self.head.next  # prior node was the head
            return
        cur = self.head
        while cur.next and cur.next.next and cur.next.next.data != value:
            cur = cur.next
        if cur.next and cur.next.next:
            cur.next = cur.next.next
        else:
            print("Value not found.")

    def delete_last(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def count(self):
        n, cur = 0, self.head
        while cur:
            n += 1
            cur = cur.next
        return n

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        items, cur = [], self.head
        while cur:
            items.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(items) + " -> None")


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid integer.")
        return None


def main():
    ll = SinglyLinkedList()
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
