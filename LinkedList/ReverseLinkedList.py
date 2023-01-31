from typing import Optional


class ListNode(object):

    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def reverseList(self,head:Optional[ListNode])-> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next=prev
            prev =curr
            curr=temp
        return prev

