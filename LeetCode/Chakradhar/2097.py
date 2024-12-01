class Node:
    def __init__(self, val):
        self.val = val
        self.nei = deque([])
        self.idg = 0

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # REF: https://www.youtube.com/watch?v=8MpoO2zA2l4
        adj = {}
        for u, v in pairs:
            if u not in adj:
                adj[u] = Node(u)
            if v not in adj:
                adj[v] = Node(v)
            adj[u].nei.append(adj[v])
            adj[v].idg += 1

        src = None
        for node in adj.values():
            if (len(node.nei) - node.idg) == 1:
                src = node
                break
        if src is None:
            src = list(adj.values())[0]

        stack = [src]
        path = []
        while stack:
            if len(stack[-1].nei) == 0:
                node = stack.pop()
                path.append(node.val)
            else:
                nei = stack[-1].nei.popleft()
                stack.append(nei)
        # path.reverse()
        ans = []
        for i in reversed(range(len(path) - 1)):
            ans.append([path[i+1], path[i]])

        return ans
