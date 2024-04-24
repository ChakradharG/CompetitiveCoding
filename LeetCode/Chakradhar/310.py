class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i: set() for i in range(n)}
        for (u, v) in edges:
            adj[u].add(v)
            adj[v].add(u)

        q = deque()
        for i in range(n):
            if len(adj[i]) <= 1:
                q.append(i)

        while n > 2:
            for _ in range(len(q)):
                u = q.popleft()
                n -= 1
                for v in adj[u]:
                    adj[v].remove(u)
                    if len(adj[v]) == 1:
                        q.append(v)

        return list(q)
