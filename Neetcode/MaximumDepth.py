class TreeNode(object):

      def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

      def maxDepth(self, root):
          return 0 if root is None else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



