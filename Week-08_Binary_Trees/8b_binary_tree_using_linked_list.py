"""Week 8 (B): Binary Tree with operations using a Linked List (nodes + pointers).

Nodes are inserted level by level (first free left/right slot), so the tree stays complete.
"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return
        q = deque([self.root])
        while q:
            cur = q.popleft()
            if not cur.left:
                cur.left = node
                return
            q.append(cur.left)
            if not cur.right:
                cur.right = node
                return
            q.append(cur.right)

    def search(self, value):
        if not self.root:
            return False
        q = deque([self.root])
        while q:
            cur = q.popleft()
            if cur.data == value:
                return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return False

    def delete(self, value):
        """Copy the deepest-rightmost node's data into the target, then remove that node."""
        if not self.root:
            print("Tree is empty.")
            return
        target, last, last_parent = None, None, None
        q = deque([(self.root, None)])
        while q:
            cur, parent = q.popleft()
            if cur.data == value and target is None:
                target = cur
            last, last_parent = cur, parent
            if cur.left:
                q.append((cur.left, cur))
            if cur.right:
                q.append((cur.right, cur))
        if target is None:
            print("Value not found.")
            return
        target.data = last.data
        if last_parent is None:
            self.root = None
        elif last_parent.right is last:
            last_parent.right = None
        else:
            last_parent.left = None

    def inorder(self, n):
        return self.inorder(n.left) + [n.data] + self.inorder(n.right) if n else []

    def preorder(self, n):
        return [n.data] + self.preorder(n.left) + self.preorder(n.right) if n else []

    def postorder(self, n):
        return self.postorder(n.left) + self.postorder(n.right) + [n.data] if n else []

    def level_order(self):
        out, q = [], deque([self.root] if self.root else [])
        while q:
            cur = q.popleft()
            out.append(cur.data)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return out

    def height(self, n):
        return 0 if not n else 1 + max(self.height(n.left), self.height(n.right))


def main():
    t = BinaryTree()
    while True:
        print("\n1. Insert  2. Delete  3. Search  4. Inorder  5. Preorder")
        print("6. Postorder  7. Level order  8. Height  9. Exit")
        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue
        if ch == 1:
            t.insert(int(input("Enter value: ")))
        elif ch == 2:
            t.delete(int(input("Enter value to delete: ")))
        elif ch == 3:
            print("Found." if t.search(int(input("Enter value to search: "))) else "Not found.")
        elif ch == 4:
            print("Inorder:", t.inorder(t.root))
        elif ch == 5:
            print("Preorder:", t.preorder(t.root))
        elif ch == 6:
            print("Postorder:", t.postorder(t.root))
        elif ch == 7:
            print("Level order:", t.level_order())
        elif ch == 8:
            print("Height:", t.height(t.root))
        elif ch == 9:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
