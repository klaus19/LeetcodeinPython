import null


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):

     def isSameTree(self, p, q):

         # If both nodes are None, they are identical
         if p is None and q is None:
             return True
         # If only one of the nodes is None, they are not identical
         if p is None or q is None:
             return False
         # Check if values are equal and recursively check left and right subtrees
         if p.val == q.val:
             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
         # Values are not equal, they are not identical
         return False

# LinkedIn
# 10
# Microsoft
# 5
# American Express
# 5
# Bloomberg
# 4
# Facebook
# 2
# Oracle
# 2
# ZScaler
# 2Amazon
# 4
# Google
# 2Apple
# 3
# Adobe
# 2

# The time complexity of this function is O(n),
# where 'n' is the total number of nodes in the larger of the two trees, p or q.
# This is because, in the worst case, the function needs to visit every node in the larger tree to determine
# if it is the same as the corresponding node in the other tree.

# The space complexity of the solution isO(min(H1,H2))O(min(H1, H2))O(min(H1,H2)),
# where H1 and H2 are the heights of the two trees, respectively.
# This is because the space used by the recursive stack is determined by the height of the smaller tree


