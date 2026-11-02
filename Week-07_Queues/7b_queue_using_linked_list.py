"""Week 7 (B): Queue using a Linked List."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        print(f"Enqueued {value}")

    def dequeue(self):
        if not self.front:
            print("Queue Underflow - queue is empty.")
            return
        print(f"Dequeued {self.front.data}")
        self.front = self.front.next
        if not self.front:
            self.rear = None

    def peek(self):
        if not self.front:
            print("Queue is empty.")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if not self.front:
            print("Queue is empty.")
            return
        items, cur = [], self.front
        while cur:
            items.append(str(cur.data))
            cur = cur.next
        print("Queue (front -> rear):", " -> ".join(items))


def main():
    q = LinkedQueue()
    while True:
        print("\n1. Enqueue  2. Dequeue  3. Peek  4. Display  5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue
        if choice == 1:
            q.enqueue(int(input("Enter value: ")))
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.peek()
        elif choice == 4:
            q.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
