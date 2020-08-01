# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        # Post order - Traversal begins
        if not root:
            return []

        stack = [root, ]
        temp, post_order = [], []
        while stack:
            node = stack.pop()
            temp.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        while temp:
            post_order.append(temp.pop())
            # Post-Order Traversal Recipe ends

        # Actual Solution begins
        output = []
        gmap = {}

        while post_order:
            output.append([])
            node = post_order.pop(0)
            if not node.left and not node.right:
                gmap[node] = 0
                output[gmap[node]].append(node.val)
            else:
                if node.left and not node.right:
                    gmap[node] = gmap[node.left] + 1
                elif node.right and not node.left:
                    gmap[node] = gmap[node.right] + 1
                else:
                    gmap[node] = max(gmap[node.left], gmap[node.right]) + 1
                output[gmap[node]].append(node.val)

        output = [c for c in output if c]
        return output