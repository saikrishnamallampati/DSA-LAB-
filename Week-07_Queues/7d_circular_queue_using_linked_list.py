"""Week 7 (D): Circular Queue using a Linked List (single rear pointer)."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedQueue:
    def __init__(self):
        self.rear = None  # rear.next is always the front

    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            node.next = node
        else:
            node.next = self.rear.next
            self.rear.next = node
        self.rear = node
        print(f"Enqueued {value}")

    def dequeue(self):
        if not self.rear:
            print("Queue Underflow - queue is empty.")
            return
        front = self.rear.next
        print(f"Dequeued {front.data}")
        if front is self.rear:
            self.rear = None
        else:
            self.rear.next = front.next

    def peek(self):
        if not self.rear:
            print("Queue is empty.")
        else:
            print("Front element:", self.rear.next.data)

    def display(self):
        if not self.rear:
            print("Queue is empty.")
            return
        items, cur = [], self.rear.next
        while True:
            items.append(str(cur.data))
            if cur is self.rear:
                break
            cur = cur.next
        print("Queue (front -> rear):", " -> ".join(items), "-> (back to front)")


def main():
    q = CircularLinkedQueue()
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
