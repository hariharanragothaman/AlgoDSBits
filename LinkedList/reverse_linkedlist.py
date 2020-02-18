class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        Function to reverse a linkedlist
        type head: ListNode
        rtype: ListNode
        """

        prev = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current

            current = next

        head = prev
        return head
