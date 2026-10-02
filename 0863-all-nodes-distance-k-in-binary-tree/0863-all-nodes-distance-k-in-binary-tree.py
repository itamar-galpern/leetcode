# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not target:
            raise ValueError("Missing target")
        first_traversal = deque([root])
        parent_dict = {root : None}
        visited = {target}
        while first_traversal:
            curr = first_traversal.popleft()
            if curr.left:
                parent_dict[curr.left] = curr
                first_traversal.append(curr.left)
            if curr.right:
                parent_dict[curr.right] = curr
                first_traversal.append(curr.right)
        if target not in parent_dict:
            raise ValueError("Target node not in this tree")
        queue = deque([target])
        level = -1

        while queue:
            level += 1
            if level == k:
                return [node.val for node in queue]
            for _ in range(len(queue)):
                curr = queue.popleft()
                parent = parent_dict[curr]
                if curr.left and curr.left not in visited:
                    visited.add(curr.left)
                    queue.append(curr.left)
                if curr.right and curr.right not in visited:
                    visited.add(curr.right)
                    queue.append(curr.right)
                if parent and parent not in visited:
                    visited.add(parent)
                    queue.append(parent)
        return []
