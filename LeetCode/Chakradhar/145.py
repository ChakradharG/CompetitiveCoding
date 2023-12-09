# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        stack, node = [], root
        while node or stack:
            while node:
                stack.append(node)
                stack.append(node.right)
                node = node.left

            node = stack.pop()  # right
            if node:
                stack.append(None)
                continue    # now the right node becomes the "center" and the process is repeated for the subtree. When the entire subtree is processed, we pop the above None so that this node's parent is then printed out (below)
            ans.append(stack.pop().val)  # center
            node = None

        return ans
