class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, w in meetings + [[0, firstPerson, 0]]:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [math.inf for _ in range(n)]
        dist[0] = 0
        h = [(0, 0)]

        while h:
            t, u = heappop(h)
            if t > dist[u]:
                continue
            for (v, w) in adj[u]:
                if t > w:
                    continue
                if w < dist[v]:
                    dist[v] = w
                    heappush(h, (w, v))

        return [i for i in range(n) if dist[i] != math.inf]
