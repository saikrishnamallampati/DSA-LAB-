"""Week 6 (A): Stack operations (Push, Pop, Peek, Display) using an Array."""


class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def push(self, value):
        if self.top == self.capacity - 1:
            print("Stack Overflow - stack is full.")
            return
        self.top += 1
        self.data[self.top] = value
        print(f"Pushed {value}")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow - stack is empty.")
            return
        print(f"Popped {self.data[self.top]}")
        self.data[self.top] = None
        self.top -= 1

    def peek(self):
        if self.top == -1:
            print("Stack is empty.")
        else:
            print("Top element:", self.data[self.top])

    def display(self):
        if self.top == -1:
            print("Stack is empty.")
            return
        print("Stack (top -> bottom):", self.data[: self.top + 1][::-1])


def main():
    size = int(input("Enter stack size: "))
    stack = ArrayStack(size)
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
