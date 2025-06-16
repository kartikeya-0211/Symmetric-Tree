from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root: TreeNode):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def preorder(root: TreeNode):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root: TreeNode):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

def levelOrderTraversal(root: TreeNode):
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        t = q.popleft()
        print(t.val, end=" ")
        if t.left:
            q.append(t.left)
        if t.right:
            q.append(t.right)

def levelOrderTraversal_t(root: TreeNode):
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        for _ in range(level_size):
            t = q.popleft()
            print(t.val, end=" ")
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        print() # New line after each level

if __name__ == "__main__":
    root = TreeNode(1)
    temp1 = TreeNode(2)
    temp2 = TreeNode(3)
    temp3 = TreeNode(4)
    temp4 = TreeNode(5)
    
    root.left = temp1
    root.right = temp2
    temp1.left = temp3
    temp2.right = temp4

    print("inOrder traversal")
    inorder(root)
    print()
    print("preOrder traversal")
    preorder(root)
    print()
    print("postOrder traversal")
    postorder(root)
    print()
    print("levelOrder traversal")
    levelOrderTraversal(root)
    print()
    print("levelOrder traversal_t")
    levelOrderTraversal_t(root)
