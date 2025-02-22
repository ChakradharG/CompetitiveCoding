# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        traversal += '-'
        stack = [(-1, TreeNode(val='dummy'))]
        i, d = 0, 0
        while i < len(traversal):
            if traversal[i] == '-':
                d += 1
                i += 1
            else:
                j = ''
                while traversal[i] != '-':
                    j += traversal[i]
                    i += 1
                cur = TreeNode(val=int(j))
                while d <= stack[-1][0]:
                    stack.pop()
                node = stack[-1][1]
                if node.left is None:
                    node.left = cur
                else:
                    node.right = cur
                stack.append((d, cur))
                d = 0

        return stack[1][1]
