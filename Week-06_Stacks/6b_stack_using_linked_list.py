"""Week 6 (B): Stack operations (Push, Pop, Peek, Display) using a Linked List."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        print(f"Pushed {value}")

    def pop(self):
        if not self.top:
            print("Stack Underflow - stack is empty.")
            return
        print(f"Popped {self.top.data}")
        self.top = self.top.next

    def peek(self):
        if not self.top:
            print("Stack is empty.")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if not self.top:
            print("Stack is empty.")
            return
        items, cur = [], self.top
        while cur:
            items.append(str(cur.data))
            cur = cur.next
        print("Stack (top -> bottom):", " -> ".join(items))


def main():
    stack = LinkedStack()
    while True:
        print("\n1. Push  2. Pop  3. Peek  4. Display  5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue
        if choice == 1:
            stack.push(int(input("Enter value: ")))
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            stack.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
