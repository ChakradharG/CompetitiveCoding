class TreeNode:
    def __init__(self, vl, ep=0, op=0):
        self.vl = vl
        self.ep = ep
        self.op = op
        self.ch = []

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        tree1 = [TreeNode(i) for i in range(n)]
        tree2 = [TreeNode(i) for i in range(m)]

        for u, v in edges1:
            tree1[u].ch.append(v)
            tree1[v].ch.append(u)
        for u, v in edges2:
            tree2[u].ch.append(v)
            tree2[v].ch.append(u)

        vis1 = set()
        def findpol1(node):
            ep, op = 1, 0
            vis1.add(node)
            for ch in tree1[node].ch:
                if ch not in vis1:
                    x, y = findpol1(ch)
                    ep += x
                    op += y
                    # print(f'{ch} -> {node} ----- {x}, {y}')
            return op, ep
        op, ep = findpol1(0)

        vis1.clear()
        def setpol1(node, ep, op):
            vis1.add(node)
            tree1[node].ep = ep
            tree1[node].op = op
            for ch in tree1[node].ch:
                if ch not in vis1:
                    setpol1(ch, op, ep)
        setpol1(0, ep, op)

        vis2 = set()
        def findpol2(node):
            ep, op = 1, 0
            vis2.add(node)
            for ch in tree2[node].ch:
                if ch not in vis2:
                    x, y = findpol2(ch)
                    ep += x
                    op += y
                    # print(f'{ch} -> {node} ----- {x}, {y}')
            return op, ep
        op, ep = findpol2(0)
        p = max(ep, op)

        ans = []
        for i in range(n):
            ans.append(p + tree1[i].ep)

        return ans
