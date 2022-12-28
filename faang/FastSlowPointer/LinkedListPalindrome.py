
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def is_Pallindrome(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    print(ListNode().is_Pallindrome(head))
