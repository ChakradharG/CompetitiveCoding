class Node:
    def __init__(self, val):
        self.val = val
        self.nei = []
        self.idg = 0    # in-degree

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for f, t in tickets:
            if f not in adj:
                adj[f] = Node(f)
            if t not in adj:
                adj[t] = Node(t)
            adj[f].nei.append(t)
            adj[t].idg += 1
        for f in adj:
            adj[f].nei = deque([adj[t] for t in sorted(adj[f].nei)])

        stack = [adj['JFK']]
        path = []
        while stack:
            if len(stack[-1].nei) == 0:
                path.append(stack.pop().val)
            else:
                stack.append(stack[-1].nei.popleft())
        path.reverse()

        return path
