class Node:
    def __init__(self, val):
        self.val = val
        self.nei = deque([])
        self.idg = 0    # in-degree

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

        # source node of eulerian path
        src = None
        for node in adj.values():
            if (len(node.nei) - node.idg) == 1:
                src = node
                break
        # is an eulerian circuit, any node can be source node
        if src is None:
            src = list(adj.values())[0]

        stack = [src]
        path = []   # valid traversal path, stored in reverse order
        while stack:
            if len(stack[-1].nei) == 0:
                # all outgoing edges visited, add this node to path now
                node = stack.pop()
                path.append(node.val)
            else:
                # visit outgoing edge
                nei = stack[-1].nei.popleft()
                stack.append(nei)

        ans = []
        # reverse the path and convert into required output format
        for i in reversed(range(len(path) - 1)):
            ans.append([path[i+1], path[i]])

        return ans
