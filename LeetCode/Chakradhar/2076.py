class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.res = [[] for _ in range(n)]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return True
        for i in range(len(self.res[b])):
            self.res[b][i] = self.find(self.res[b][i])
            if a == self.res[b][i]:
                return False
        self.par[b] = a
        self.res[a] += self.res[b]
        self.res[b] = []
        return True

    def find(self, a):
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]

    def block(self, a, b):
        self.res[a].append(b)
        self.res[b].append(a)


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)

        for x, y in set(((min(x, y), max(x, y)) for x, y in restrictions)):
            dsu.block(x, y)

        ans = []
        for u, v in requests:
            ans.append(dsu.union(min(u, v), max(u, v)))

        return ans

