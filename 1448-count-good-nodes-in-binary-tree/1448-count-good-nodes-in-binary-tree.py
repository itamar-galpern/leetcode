# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -math.inf)

    def dfs(self, node, max_val):
        if not node:
            return 0
        if node.val >= max_val:
            left_dfs = self.dfs(node.left, node.val) if node.left else 0
            right_dfs = self.dfs(node.right, node.val) if node.right else 0
            return 1 + left_dfs + right_dfs
        left_dfs = self.dfs(node.left, max_val) if node.left else 0
        right_dfs = self.dfs(node.right, max_val) if node.right else 0
        return left_dfs + right_dfs
        
        