# To find a diameter of a tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        gmap = {}
        diameter = 0

        # Post-Order Traversal recipe
        q = deque([])
        res_temp = []

        if not root:
            return 0

        stack = [root, ]

        while stack:
            node = stack.pop()
            res_temp.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        while res_temp:
            q.append(res_temp.pop())
            # End of Post-order recipe

        left, right = 0, 0
        while q:
            node = q.popleft()
            left = gmap[node.left] if node.left else 0
            right = gmap[node.right] if node.right else 0
            diameter = max(diameter, left + right)
            gmap[node] = max(left, right) + 1

        return diameter