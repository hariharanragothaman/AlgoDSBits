class Solution:
    def getDecimalValue(self, head):
        ll = []
        curr = head
        while curr:
            ll.append(curr.val)
            curr = curr.next
        ss = ''.join(str(c) for c in ll)
        result = (int(ss, 2))   # This is converting a integer to binary
        return result
