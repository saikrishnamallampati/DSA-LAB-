"""Week 7 (C): Circular Queue using Arrays."""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            print("Queue Overflow - queue is full.")
            return
        rear = (self.front + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1
        print(f"Enqueued {value}")

    def dequeue(self):
        if self.size == 0:
            print("Queue Underflow - queue is empty.")
            return
        print(f"Dequeued {self.data[self.front]}")
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def peek(self):
        if self.size == 0:
            print("Queue is empty.")
        else:
            print("Front element:", self.data[self.front])

    def display(self):
        if self.size == 0:
            print("Queue is empty.")
            return
        items = [self.data[(self.front + i) % self.capacity] for i in range(self.size)]
        print("Queue (front -> rear):", items)


def main():
    q = CircularQueue(int(input("Enter queue size: ")))
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
