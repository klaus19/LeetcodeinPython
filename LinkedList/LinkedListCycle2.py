class Solution(object):
    def detectCycle(self, head):

        if not head or head.next:
            return "no cycle"

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:

    # if they are equal it means there is a cycle in the list, and now you have to reset slow as the head
               slow = head
               while slow!=fast:
                   slow = slow.next
                   fast = fast.next
               return slow
        return None

