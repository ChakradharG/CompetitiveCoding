class Solution:
    def propUpward(self, u: int) -> Tuple[int, int]:
        for v in self.graph[u][0]:
            self.graph[v][0].discard(u)
            n, d = self.propUpward(v)
            self.graph[u][1] += n
            self.graph[u][2] += n + d
        return self.graph[u][1], self.graph[u][2]

    def propDownward(self, u: int, p: int) -> None:
        d = self.graph[p][2] - (self.graph[u][1] + self.graph[u][2])
        self.graph[u][2] += (self.n - self.graph[u][1]) + d
        for v in self.graph[u][0]:
            self.propDownward(v, u)

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.n = n
        self.graph = [[set(), 1, 0] for _ in range(n)] # [neighbors, nodes in subtree, sum of distances]
        for u, v in edges:
            self.graph[u][0].add(v)
            self.graph[v][0].add(u)

        self.propUpward(0)
        for v in self.graph[0][0]:
            self.propDownward(v, 0)

        return [node[2] for node in self.graph]
