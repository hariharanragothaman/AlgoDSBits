from collections import deque


# Binary Tree Implementation [Regular Binary Tree Implementations]

# Definition of Tree Node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root):
        result = []
        level = 0

        if not root:
            return result

        # Put the entire Tree into a Queue
        q = deque([root])

        while q:
            result.append([])
            level_length = len(q)
            print("The levels is:", level_length)
            print("Q now is:", q)

            # For the length of levels
            for i in range(level_length):
                node = q.popleft()
                print("The node is:", node)
                print("The Q now is:", q)
                # in the current level - add the root
                result[level].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                print("The result is:", result)
                print("The queue now is:", q)
            print("***************************")
            level += 1

        print("The total number of levels is:", level)
        return result


# Constructing the Binary Tree by hand
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
sol = Solution()
res = sol.level_order(root)
print("The binary tree level order is", res)
