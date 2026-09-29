# Circular Queue using Array and Linked List


# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Queue Class
class CircularQueue:

    def __init__(self, size):
        # Array Queue
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

        # Linked List Queue
        self.ll_front = None
        self.ll_rear = None

    # ================= ARRAY CIRCULAR QUEUE =================

    def array_enqueue(self):
        data = int(input("Enter element: "))

        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        # First element
        if self.front == -1:
            self.front = 0
            self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data

        print("Element inserted successfully")

    def array_dequeue(self):

        if self.front == -1:
            print("Queue is empty")
            return

        data = self.queue[self.front]

        self.queue[self.front] = None

        print("Deleted element:", data)

        # Only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        else:
            self.front = (self.front + 1) % self.size

    def array_peek(self):

        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    def array_display(self):

        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue elements:")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()

    # ================= LINKED LIST CIRCULAR QUEUE =================

    def linked_enqueue(self):
        data = int(input("Enter element: "))

        new_node = Node(data)

        # Queue is empty
        if self.ll_front is None:

            self.ll_front = new_node
            self.ll_rear = new_node

            # Point rear to front
            self.ll_rear.next = self.ll_front

        else:

            # Insert new node after rear
            new_node.next = self.ll_front
            self.ll_rear.next = new_node

            # Move rear
            self.ll_rear = new_node

        print("Element inserted successfully")

    def linked_dequeue(self):

        if self.ll_front is None:
            print("Queue is empty")
            return

        data = self.ll_front.data

        print("Deleted element:", data)

        # Only one node
        if self.ll_front == self.ll_rear:

            self.ll_front = None
            self.ll_rear = None

        else:

            self.ll_front = self.ll_front.next
            self.ll_rear.next = self.ll_front

    def linked_peek(self):

        if self.ll_front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.ll_front.data)

    def linked_display(self):

        if self.ll_front is None:
            print("Queue is empty")
            return

        print("Queue elements:")

        temp = self.ll_front

        while True:

            print(temp.data, end=" ")

            temp = temp.next

            if temp == self.ll_front:
                break

        print()


# ================= MAIN PROGRAM =================

size = int(input("Enter size of Array Circular Queue: "))

q = CircularQueue(size)


while True:

    print("\n========== MAIN MENU ==========")
    print("1. Circular Queue using Array")
    print("2. Circular Queue using Linked List")
    print("3. Exit")
    print("===============================")

    choice = int(input("Enter your choice: "))


    # ================= ARRAY MENU =================

    if choice == 1:

        while True:

            print("\n------ ARRAY CIRCULAR QUEUE ------")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")
            print("----------------------------------")

            option = int(input("Enter your choice: "))

            if option == 1:
                q.array_enqueue()

            elif option == 2:
                q.array_dequeue()

            elif option == 3:
                q.array_peek()

            elif option == 4:
                q.array_display()

            elif option == 5:
                break

            else:
                print("Invalid choice")


    # ================= LINKED LIST MENU =================

    elif choice == 2:

        while True:

            print("\n--- LINKED LIST CIRCULAR QUEUE ---")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")
            print("----------------------------------")

            option = int(input("Enter your choice: "))

            if option == 1:
                q.linked_enqueue()

            elif option == 2:
                q.linked_dequeue()

            elif option == 3:
                q.linked_peek()

            elif option == 4:
                q.linked_display()

            elif option == 5:
                break

            else:
                print("Invalid choice")


    # ================= EXIT =================

    elif choice == 3:

        print("Program ended")
        break

    else:

        print("Invalid choice")