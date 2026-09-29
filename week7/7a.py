# Queue Implementation using Array and Linked List

# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class
class Queue:

    def __init__(self):
        # Array Queue
        self.queue = []

        # Linked List Queue
        self.front = None
        self.rear = None

    # ================= ARRAY QUEUE =================

    def array_enqueue(self):
        data = int(input("Enter element: "))
        self.queue.append(data)
        print("Element inserted successfully.")

    def array_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            data = self.queue.pop(0)
            print("Deleted element:", data)

    def array_peek(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[0])

    def array_display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:")
            for element in self.queue:
                print(element, end=" ")
            print()

    # ================= LINKED LIST QUEUE =================

    def linked_enqueue(self):
        data = int(input("Enter element: "))

        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Element inserted successfully.")

    def linked_dequeue(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            data = self.front.data

            self.front = self.front.next

            if self.front is None:
                self.rear = None

            print("Deleted element:", data)

    def linked_peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element:", self.front.data)

    def linked_display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            temp = self.front

            print("Queue elements:")

            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()


# ================= MAIN PROGRAM =================

q = Queue()

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Queue using Array")
    print("2. Queue using Linked List")
    print("3. Exit")
    print("===============================")

    choice = int(input("Enter your choice: "))

    # ================= ARRAY MENU =================

    if choice == 1:

        while True:

            print("\n------ QUEUE USING ARRAY ------")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")
            print("-------------------------------")

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
                print("Invalid choice.")

    # ================= LINKED LIST MENU =================

    elif choice == 2:

        while True:

            print("\n--- QUEUE USING LINKED LIST ---")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")
            print("-------------------------------")

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
                print("Invalid choice.")

    # ================= EXIT =================

    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")