# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node, cam, pcam):
            if node is None:
                if cam:
                    return math.inf
                else:
                    return 0
            res = dfs(node.left, 0, cam) + dfs(node.right, 0, cam) if (cam or pcam) else math.inf
            res = min(
                res,
                2 + dfs(node.left, 1, cam) + dfs(node.right, 1, cam),
                1 + dfs(node.left, 0, cam) + dfs(node.right, 1, cam),
                1 + dfs(node.left, 1, cam) + dfs(node.right, 0, cam),
            )
            return res

        return min(1 + dfs(root, 1, 0), dfs(root, 0, 0))

