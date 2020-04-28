"""
Add 2 numbers - given in the form a Linked List
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, ):
        self.head = None
        self.tail = None
        return

    def push_elements(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return

    def display(self):
        print("Displaying the LinkedList")
        current = self.head
        while current:
            print("The value is:", current.val)
            current = current.next
        return


class Solution:
    def add_two_numbers(self, list1, list2):

        l1 = list1
        l2 = list2

        carry = 0
        dummy = Node(0)
        current = dummy    # Because finally we want to return - dummy.next

        # Number lengths can be different and there can be extra carry bit
        while l1 or l2 or carry:
            # Selecting the values to add
            if l1 is not None:
                value1 =  l1.val
            else:
                value1 = 0

            if l2 is not None:
                value2 = l2.val
            else:
                value2 = 0

            # Adding Logic:
            add = value1 + value2 + carry
            carry = add // 10
            item = add % 10

            current.next = Node(item)
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

if __name__ == '__main__':

    # ---- First number
    s1 = Node(3)
    s2 = Node(4)
    s3 = Node(5)
    t1 = LinkedList()
    t1.push_elements(s1)
    t1.push_elements(s2)
    t1.push_elements(s3)
    t1.display()

    # ---- Second number
    v1 = Node(6)
    v2 = Node(7)
    v3 = Node(8)
    t2 = LinkedList()
    t2.push_elements(v1)
    t2.push_elements(v2)
    t2.push_elements(v3)
    t2.display()

    sol = Solution()
    result = sol.add_two_numbers(s1, v1)