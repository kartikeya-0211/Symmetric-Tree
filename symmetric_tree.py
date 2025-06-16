class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SymmetricTree:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._isMirror(root.left, root.right)

    def _isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val) and \
               self._isMirror(left.left, right.right) and \
               self._isMirror(left.right, right.left)

if __name__ == "__main__":
    root = TreeNode(1)
    temp1 = TreeNode(2)
    temp2 = TreeNode(2)
    temp3 = TreeNode(3)
    temp4 = TreeNode(3)
    temp5 = TreeNode(4)
    temp6 = TreeNode(4)

    root.left = temp1
    root.right = temp2
    temp1.left = temp3
    temp1.right = temp5
    temp2.left = temp6
    temp2.right = temp4

    st = SymmetricTree()
    ans = st.isSymmetric(root)
    print(ans)
