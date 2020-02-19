class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def pushElements(self, item):
        """
        Function to push elements into a SLL
        P.S This function is like super important
        """

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def reverseList(self):
        """
        Function to reverse a linkedlist
        type head: ListNode
        rtype: ListNode
        """
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def display(self):
        curr = self.head
        while curr:
            print (curr.val)
            curr = curr.next
        return


if __name__ == '__main__':
    s1 = ListNode(5)
    s2 = ListNode(6)
    s3 = ListNode(7)
    s4 = ListNode(8)

    t1 = Solution()

    t1.pushElements(s1)
    t1.pushElements(s2)
    t1.pushElements(s3)
    t1.pushElements(s4)

    t1.display()
    print("Reversing the List")
    t1.reverseList()
    t1.display()
