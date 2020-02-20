class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def pushElements(self, item):
        # (object, class)
        if not isinstance(item, ListNode):
            self.item = ListNode(item)

        if self.head == None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return

    def display(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def deleteNode(self, data):
        prev = None
        curr = self.head
        while curr:
            if curr.next.val == data:
                curr.next = curr.next.next
                break
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

    t1.deleteNode(6)

    print("**********")

    t1.display()
