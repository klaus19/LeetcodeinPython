from collections import deque

from Trees.TreeNode import TreeNode


class Solution(object):

    def max_Depth(self,root:TreeNode) -> int:
         if not root:
             return 0
         return 1+max(self.max_Depth(root.left),self.max_Depth(root.right))

    # secomd method BFS
    def max_depth_bfs(self,root:TreeNode) -> int:
        if not root:
            return 0

        level=1
        q = deque([root])
        while q:
         for i in range(len(q)):
             node = q.popleft()
             if node.left:
                 q.append(node.left)
             if node.right:
                 q.append(node.right)
         level += 1
        return level

    # third iterative dfs

    def max_depth_dfs(self,root:TreeNode) -> int:
        if not root:
            return 0

        stack = [[root,1]]
        res=1
        while stack:
            node,depth = stack.pop()

            if node:
                res = max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res
