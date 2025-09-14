from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val and
                self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))

# Example symmetric tree:
#       1
#     /   \
#    2     2
#   / \   / \
#  3   4 4   3

root = TreeNode(1,
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3)))

sol = Solution()
print(sol.isSymmetric(root))  # Output: True
