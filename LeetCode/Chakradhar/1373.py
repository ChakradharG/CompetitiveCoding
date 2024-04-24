# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):  # is subtree valid, sum, min, max, ans
            if not node.left:
                lValid, lSum, lMin, lMax, lAns = (True, 0, node.val, -math.inf, 0)
            else:
                lValid, lSum, lMin, lMax, lAns = dfs(node.left)

            if not node.right:
                rValid, rSum, rMin, rMax, rAns = (True, 0, math.inf, node.val, 0)
            else:
                rValid, rSum, rMin, rMax, rAns = dfs(node.right)

            if not (lValid and rValid and lMax < node.val < rMin):
                return (False, 0, 0, 0, max(lAns, rAns))

            ans = max(lAns, rAns, lSum+node.val+rSum)

            return (True, (lSum+node.val+rSum), lMin, rMax, ans)

        return dfs(root)[-1]
