class Solution(object):

    def removeElements(self, head, val):

        curr_node,previous_node = head,None

        while curr_node:
            if curr_node.val == val:
        # need to delete current node
                if curr_node == head:
                    curr_node = head =head.next
                else:
                    previous_node.next = curr_node.next
                    curr_node = curr_node.next
            else:
                previous_node = curr_node
                curr_node = curr_node.next
        return head

