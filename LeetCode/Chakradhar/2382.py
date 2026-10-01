class DSU:
    def __init__(self, n):
        self.par = list(range(2*n+1))
        self.val = [0] * (2*n+1)

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        self.par[b] = a
        self.val[a] += self.val[b]
        return self.val[a]

    def find(self, a):
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]

    def add(self, a, v):
        a = 2 * a + 1
        self.val[a] = v
        self.union(a, a+1)
        return self.union(a-1, a)


class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        n = len(removeQueries)
        dsu = DSU(n)

        ans = [0] * n
        h = 0
        for i in reversed(range(n)):
            ans[i] = h
            j = removeQueries[i]
            h = max(h, dsu.add(j, nums[j]))

        return ans

