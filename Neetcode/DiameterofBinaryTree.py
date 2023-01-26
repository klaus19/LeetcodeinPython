class Node:

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    def diamter(self,root):
        self.ans=1
        def depth(p):
            if not p:return 0
            left,right = depth(p.left),depth(p.right)
            self.ans = max(self.ans,left+right+1)
            return max(left,right)+1
        depth(root)
        return self.ans-1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(Node().diamter(root))

