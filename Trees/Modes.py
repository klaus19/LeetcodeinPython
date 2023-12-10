class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def findMode(self, root):
        hashmap = {}
        res = []

        def dfs(root):
            if not root:
                return None

            if root.val not in hashmap:
                hashmap[root.val] =1
            else:
                hashmap[root.val]+=1

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        mode_list = max(list(hashmap.values()))
        for key,value in hashmap.items():
            if value == mode_list:
                res.append(key)

        return res

