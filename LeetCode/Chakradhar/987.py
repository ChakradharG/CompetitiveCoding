# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}  # col: {row: [vals]}
        q = deque([(root, 0, 0)])
        while q:
            node, r, c = q.popleft()
            if node is None:
                continue
            if c not in d:
                d[c] = {}
            if r not in d[c]:
                d[c][r] = []
            d[c][r].append(node.val)
            q.append((node.left, r+1, c-1))
            q.append((node.right, r+1, c+1))

        ans = []
        for c in sorted(d.keys()):
            temp = []
            for r in d[c]:
                temp.extend(sorted(d[c][r]))
            ans.append(temp)

        return ans
