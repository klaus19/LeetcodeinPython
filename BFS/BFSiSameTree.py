class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isSameTree(self,p,q):

        if not p and not q: return True

        if not p or not q: return False

        queue_p = [p]
        queue_q = [q]

        while queue_p and queue_q:

              node_p = queue_p.pop(0)
              node_q = queue_q.pop(0)

              if node_p.val != node_q.val: return False

              if node_p.left and node_q.left:
                 queue_p.append(node_p.left)
                 queue_q.append(node_q.left)
              elif node_p.left or node_q.left:
                 return False

              if node_p.right and node_q.right:
                 queue_p.append(node_p.right)
                 queue_q.append(node_q.right)
              elif node_p.right or node_q.right:
                 return False
        return True

