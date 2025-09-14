from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
        if root:
            todo = [root]
            result = []
            while todo:
                node = todo.pop()
                result.append(node.val)
                if node.right:
                    todo.append(node.right)
                if node.left:
                    todo.append(node.left)
            return result
        else:
            return []
    
#No Output Code Is Written.