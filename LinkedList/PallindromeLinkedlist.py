class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next


class Solution(object):
    def isPalindrome(self, head):
        node,vals = head,[head.val]
        while node.next:
            node = node.next
            vals.append(node.val)
        return vals == vals[::-1]