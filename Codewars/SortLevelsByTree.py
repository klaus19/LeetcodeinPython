
class Solution(object):
 def tree_by_levels(tree):
    queue = [tree]
    values = []

    while queue:
        node = queue.pop(0)
        if node:
            queue += [node.left, node.right]
            values.append(node.value)

    return values
