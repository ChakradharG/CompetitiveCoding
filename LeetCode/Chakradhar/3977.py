class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))

        distT = [inf] * n
        distP = [-inf] * n
        distT[source] = 0
        distP[source] = power

        h = [(0, -power, source)]
        while h:
            t, p, u = heappop(h)
            p *= -1
            if u == target:
                return [t, p]
            p -= cost[u]
            if p < 0:
                continue
            for v, dt in graph[u]:
                nt = t + dt
                if (nt < distT[v]) or (p > distP[v]):
                    distT[v] = nt
                    distP[v] = p
                    heappush(h, (nt, -p, v))

        return [-1, -1]
