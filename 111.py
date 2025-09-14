from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


# Example tree:
#     3
#    / \
#   9  20
#      / \
#     15  7

root = TreeNode(3,
                TreeNode(9),
                TreeNode(20, TreeNode(15), TreeNode(7)))

sol = Solution()
print(sol.minDepth(root))  # Output: 2