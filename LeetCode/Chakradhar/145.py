# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = deque([])

        stack, node = [], root
        while node or stack:
            while node:
                ans.appendleft(node.val)
                stack.append(node)
                node = node.right

            node = stack.pop().left

        return ans
