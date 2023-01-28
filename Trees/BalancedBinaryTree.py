class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:
    def checkHeight(node: TreeNode) -> int:
        if not node:
            return 0
        leftHeight = checkHeight(node.left)
        if leftHeight == -1:
            return -1
        rightHeight = checkHeight(node.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

    return checkHeight(root) != -1
