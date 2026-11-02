"""Week 10: AVL Tree (self-balancing BST) with all its operations."""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def height(self, n):
        return n.height if n else 0

    def balance(self, n):
        return self.height(n.left) - self.height(n.right) if n else 0

    def update(self, n):
        n.height = 1 + max(self.height(n.left), self.height(n.right))

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self.update(y)
        self.update(x)
        return x

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self.update(x)
        self.update(y)
        return y

    def rebalance(self, n):
        self.update(n)
        b = self.balance(n)
        if b > 1:  # left heavy
            if self.balance(n.left) < 0:  # Left-Right case
                n.left = self.rotate_left(n.left)
            return self.rotate_right(n)  # Left-Left case
        if b < -1:  # right heavy
            if self.balance(n.right) > 0:  # Right-Left case
                n.right = self.rotate_right(n.right)
            return self.rotate_left(n)  # Right-Right case
        return n

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print("Duplicate keys are not allowed.")
            return root
        return self.rebalance(root)

    def min_node(self, n):
        while n.left:
            n = n.left
        return n

    def delete(self, root, key):
        if root is None:
            print("Key not found.")
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ = self.min_node(root.right)
            root.key = succ.key
            root.right = self.delete(root.right, succ.key)
        return self.rebalance(root)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        return self.search(root.left if key < root.key else root.right, key)

    def inorder(self, r):
        return self.inorder(r.left) + [r.key] + self.inorder(r.right) if r else []

    def preorder(self, r):
        return [r.key] + self.preorder(r.left) + self.preorder(r.right) if r else []

    def postorder(self, r):
        return self.postorder(r.left) + self.postorder(r.right) + [r.key] if r else []

    def display(self, r, level=0):
        """Sideways print of the tree (right subtree on top)."""
        if r:
            self.display(r.right, level + 1)
            print("    " * level + f"{r.key} (bf={self.balance(r)})")
            self.display(r.left, level + 1)


def main():
    t, root = AVLTree(), None
    while True:
        print("\n1. Insert  2. Delete  3. Search  4. Inorder  5. Preorder  6. Postorder")
        print("7. Height  8. Display tree  9. Exit")
        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue
        if ch == 1:
            root = t.insert(root, int(input("Enter key: ")))
        elif ch == 2:
            root = t.delete(root, int(input("Enter key to delete: ")))
        elif ch == 3:
            print("Found." if t.search(root, int(input("Enter key to search: "))) else "Not found.")
        elif ch == 4:
            print("Inorder:", t.inorder(root))
        elif ch == 5:
            print("Preorder:", t.preorder(root))
        elif ch == 6:
            print("Postorder:", t.postorder(root))
        elif ch == 7:
            print("Height:", t.height(root))
        elif ch == 8:
            t.display(root) if root else print("Tree is empty.")
        elif ch == 9:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
