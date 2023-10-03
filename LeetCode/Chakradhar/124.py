# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, float("-inf")
            
            leftPathH, leftMax = dfs(node.left)
            rightPathH, rightMax = dfs(node.right)

            pathH = max(
                leftPathH + node.val,
                rightPathH + node.val,
                node.val
            )

            currMax = max(
                leftMax,
                rightMax,
                pathH,
                leftPathH + node.val + rightPathH
            )

            # maxSum = max(node.val + leftHeightSum + rightHeightSum,
            # node.val + leftHeightSum,
            # node.val + rightHeightSum)
            # return node.val + max(leftHeightSum, rightHeightSum), max(leftSum, rightSum, maxSum, node.val)
            return pathH, currMax
        
        return dfs(root)[1]