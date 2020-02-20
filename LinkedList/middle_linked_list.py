"""
Middle of LinkedList
"""

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
        if not isinstance(item, ListNode):
            item = Listnode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def display(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def middle_linked_list(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    s1 = ListNode(5)
    s2 = ListNode(6)
    s3 = ListNode(7)
    s4 = ListNode(8)
    s5 = ListNode(9)


    t1 = Solution()
    t1.pushElements(s1)
    t1.pushElements(s2)
    t1.pushElements(s3)
    t1.pushElements(s4)
    t1.pushElements(s5)

    t1.display()

    result = t1.middle_linked_list()
    print(result.val)
