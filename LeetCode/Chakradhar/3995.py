class Solution:
    def findAll(self, source: str, target: str, pattern: str, replacement: str) -> list[int]:
        res = []
        l = len(pattern)
        for i in range(len(source)-l+1):
            for j in range(l):
                if (pattern[j] != "*" and pattern[j] != source[i+j]) or (replacement[j] != target[i+j]):
                    break
            else:
                res.append(i)
        return res

    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        if len(source) != len(target):
            return -1
        n = len(source)
        m = len(rules)

        applicable = [[] for _ in range(n)]
        starCount = [0 for _ in range(m)]
        for k in range(m):
            starCount[k] += rules[k][0].count("*")
            for i in self.findAll(source, target, rules[k][0], rules[k][1]):
                applicable[i].append(k)

        @cache
        def dfs(i):
            if i == n:
                return 0
            ans = inf
            if source[i] == target[i]:
                ans = dfs(i+1)
            for k in applicable[i]:
                ans = min(ans, starCount[k] + costs[k] + dfs(i+len(rules[k][0])))
            return ans

        ans = dfs(0)
        if ans == inf:
            return -1
        return ans

