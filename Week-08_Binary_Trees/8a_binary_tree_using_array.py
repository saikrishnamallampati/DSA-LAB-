"""Week 8 (A): Binary Tree with operations using an Array.

Array representation: node at index i has children at 2i+1 (left) and 2i+2 (right).
The tree is kept complete - new nodes are inserted at the next free position.
"""


class ArrayBinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        self.tree.append(value)

    def search(self, value):
        return self.tree.index(value) if value in self.tree else -1

    def delete(self, value):
        """Replace the node with the last element, then drop the last slot."""
        if value not in self.tree:
            print("Value not found.")
            return
        i = self.tree.index(value)
        self.tree[i] = self.tree[-1]
        self.tree.pop()

    def inorder(self, i=0):
        if i >= len(self.tree):
            return []
        return self.inorder(2 * i + 1) + [self.tree[i]] + self.inorder(2 * i + 2)

    def preorder(self, i=0):
        if i >= len(self.tree):
            return []
        return [self.tree[i]] + self.preorder(2 * i + 1) + self.preorder(2 * i + 2)

    def postorder(self, i=0):
        if i >= len(self.tree):
            return []
        return self.postorder(2 * i + 1) + self.postorder(2 * i + 2) + [self.tree[i]]

    def level_order(self):
        return list(self.tree)

    def height(self, i=0):
        if i >= len(self.tree):
            return 0
        return 1 + max(self.height(2 * i + 1), self.height(2 * i + 2))

    def display(self):
        if not self.tree:
            print("Tree is empty.")
            return
        for i, v in enumerate(self.tree):
            left = self.tree[2 * i + 1] if 2 * i + 1 < len(self.tree) else None
            right = self.tree[2 * i + 2] if 2 * i + 2 < len(self.tree) else None
            print(f"Index {i}: {v}  (left={left}, right={right})")


def main():
    t = ArrayBinaryTree()
    while True:
        print("\n1. Insert  2. Delete  3. Search  4. Inorder  5. Preorder")
        print("6. Postorder  7. Level order  8. Height  9. Display array  10. Exit")
        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 10.")
            continue
        if ch == 1:
            t.insert(int(input("Enter value: ")))
        elif ch == 2:
            t.delete(int(input("Enter value to delete: ")))
        elif ch == 3:
            pos = t.search(int(input("Enter value to search: ")))
            print("Not found." if pos == -1 else f"Found at index {pos}.")
        elif ch == 4:
            print("Inorder:", t.inorder())
        elif ch == 5:
            print("Preorder:", t.preorder())
        elif ch == 6:
            print("Postorder:", t.postorder())
        elif ch == 7:
            print("Level order:", t.level_order())
        elif ch == 8:
            print("Height:", t.height())
        elif ch == 9:
            t.display()
        elif ch == 10:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
