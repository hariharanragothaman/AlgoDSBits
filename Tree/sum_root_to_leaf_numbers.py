# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, '')]
        result = []
        while stack:
            node, val = stack.pop()
            val += str(node.val)

            if not node.left and not node.right:
                result.append(val)

            if node.left:
                stack.append((node.left, val))
            if node.right:
                stack.append((node.right, val))

        result = sum(int(c) for c in result)
        return result