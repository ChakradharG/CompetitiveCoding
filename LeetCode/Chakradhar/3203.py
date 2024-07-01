class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def minHeight(edges):
            adj = defaultdict(set)
            for (u, v) in edges:
                adj[u].add(v)
                adj[v].add(u)

            n = len(adj)
            q = deque()
            for i in range(n):
                if len(adj[i]) <= 1:
                    q.append(i)

            h = 0
            while n > 2:
                for _ in range(len(q)):
                    u = q.popleft()
                    n -= 1
                    for v in adj[u]:
                        adj[v].remove(u)
                        if len(adj[v]) == 1:
                            q.append(v)
                h += 1

            return h + (len(q) - 1), 2*h + (len(q) - 1)

        x1, y1 = minHeight(edges1)
        x1 = max(0, x1)
        x2, y2 = minHeight(edges2)
        x2 = max(0, x2)

        return max(
            y1, y2,
            x1 + 1 + x2
        )
