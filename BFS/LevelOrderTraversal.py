import collections


class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        res=[]
        queue = collections.deque

        queue.append(root)

        while queue:
            qLen = len(queue)
            level =[]
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
               res.append(level)
        return res