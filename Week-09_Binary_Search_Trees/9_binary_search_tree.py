"""Week 9: Binary Search Tree (BST) operations."""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

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

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def min_node(self, root):
        while root.left:
            root = root.left
        return root

    def max_node(self, root):
        while root.right:
            root = root.right
        return root

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
            succ = self.min_node(root.right)  # inorder successor
            root.key = succ.key
            root.right = self.delete(root.right, succ.key)
        return root

    def inorder(self, r):
        return self.inorder(r.left) + [r.key] + self.inorder(r.right) if r else []

    def preorder(self, r):
        return [r.key] + self.preorder(r.left) + self.preorder(r.right) if r else []

    def postorder(self, r):
        return self.postorder(r.left) + self.postorder(r.right) + [r.key] if r else []

    def height(self, r):
        return 0 if r is None else 1 + max(self.height(r.left), self.height(r.right))


def main():
    t = BST()
    while True:
        print("\n1. Insert  2. Delete  3. Search  4. Inorder  5. Preorder  6. Postorder")
        print("7. Minimum  8. Maximum  9. Height  10. Exit")
        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 10.")
            continue
        if ch == 1:
            t.root = t.insert(t.root, int(input("Enter key: ")))
        elif ch == 2:
            t.root = t.delete(t.root, int(input("Enter key to delete: ")))
        elif ch == 3:
            print("Found." if t.search(t.root, int(input("Enter key to search: "))) else "Not found.")
        elif ch == 4:
            print("Inorder:", t.inorder(t.root))
        elif ch == 5:
            print("Preorder:", t.preorder(t.root))
        elif ch == 6:
            print("Postorder:", t.postorder(t.root))
        elif ch == 7:
            print("Minimum:", t.min_node(t.root).key if t.root else "Tree is empty.")
        elif ch == 8:
            print("Maximum:", t.max_node(t.root).key if t.root else "Tree is empty.")
        elif ch == 9:
            print("Height:", t.height(t.root))
        elif ch == 10:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
