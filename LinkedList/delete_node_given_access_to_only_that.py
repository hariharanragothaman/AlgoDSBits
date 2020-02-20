class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SLL():
    def __init__(self):
        self.head = None
        self.tail = None

    def pushElements(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            item = self.head
        else:
            self.tail.next = item
        self.tail = item

    def display(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.nex

    def deleteNode(self, node):
        """
        The idea is to replace the elements instead of deleting
        """
        node.val = node.next.val
        node.next = node.next.next
