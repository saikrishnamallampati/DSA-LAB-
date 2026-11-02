"""Week 7 (A): Queue using Arrays (linear queue)."""


class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = -1

    def enqueue(self, value):
        if self.rear == self.capacity - 1:
            print("Queue Overflow - queue is full.")
            return
        self.rear += 1
        self.data[self.rear] = value
        print(f"Enqueued {value}")

    def dequeue(self):
        if self.front > self.rear:
            print("Queue Underflow - queue is empty.")
            return
        print(f"Dequeued {self.data[self.front]}")
        self.front += 1

    def peek(self):
        if self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Front element:", self.data[self.front])

    def display(self):
        if self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Queue (front -> rear):", self.data[self.front : self.rear + 1])


def main():
    q = ArrayQueue(int(input("Enter queue size: ")))
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
