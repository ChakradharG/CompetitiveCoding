class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        adj = {(i+1): set() for i in range(n)}
        for (u, v) in edges:
            adj[u].add(v)
            adj[v].add(u)

        q = deque([(1, 1)])
        for s in range(t):
            for _ in range(len(q)):
                u, p = q.popleft()
                if len(adj[u]) == 0:
                    q.append((u, p))
                else:
                    x = len(adj[u])
                    for v in adj[u]:
                        adj[v].remove(u)
                        q.append((v, p*(1/x)))

        for (u, p) in q:
            if u == target:
                return p

        return 0
