class Solution(object):

    def __init__(self,val=0,left=None,right=None):
             self.val = val
             self.left = left
             self.right = right

    class Inorder(object):
        def Inorder(self,root):

            return [] if not root else self.Inorder(root.left) + [root.val] + self.Inorder(root.right)

# Microsoft
# 7
# Facebook
# 5
# Google
# 4
# Apple
# 4
# Oracle
# 2
# Bloomberg
# 2
# Yahoo
# 2
# Goldman Sachs
# 2

# The time complexity of the Inorder method for performing an inorder traversal of a binary tree is O(n),
# where 'n' is the number of nodes in the binary tree.
# The space complexity of the Inorder method for performing an inorder traversal of a binary tree is O(h),
# where 'h' is the height of the binary tree.