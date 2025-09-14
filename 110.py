from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root) != -1

    def checkHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        leftHeight = self.checkHeight(node.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.checkHeight(node.right)
        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1
    
    
# Example balanced tree:
#       3
#      / \
#     9  20
#        / \
#       15  7

root = TreeNode(3,
                TreeNode(9),
                TreeNode(20, TreeNode(15), TreeNode(7)))

sol = Solution()
print(sol.isBalanced(root))  # Output: True
