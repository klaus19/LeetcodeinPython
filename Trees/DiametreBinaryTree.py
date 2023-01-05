from typing import Optional

from Trees.TreeNode import TreeNode


class Solution(object):
    diameter = 0

    def getMaxDepth(self, root):
        if not root:
            return 0
        leftSubtreeDepth = self.getMaxDepth(root.left)
        rightSubtreeDepth = self.getMaxDepth(root.right)
        self.diameter = max(self.diameter, leftSubtreeDepth + rightSubtreeDepth)
        return max(rightSubtreeDepth, leftSubtreeDepth) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.getMaxDepth(root)
        return self.diameter
