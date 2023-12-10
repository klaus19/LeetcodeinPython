from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(self,root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_values = []
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()
            level_values.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(level_values)

    return result

if __name__ == "__main__":
   root = TreeNode(3)
   root.left = TreeNode(9)
   root.right = TreeNode(20)
   root.right.left = TreeNode(15)
   root.right.right = TreeNode(7)

# Perform level order traversal
   result = level_order_traversal(root)
   print(result)
