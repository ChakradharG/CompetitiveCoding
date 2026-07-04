class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        MOD = 10**9 + 7
        n1, n2, nt = len(word1), len(word2), len(target)

        @cache
        def dfs(p1, p2, pt):
            if pt == nt:
                return int(p1>0 and p2>0)
            res = 0
            for i in range(p1, n1):
                if word1[i] == target[pt]:
                    res = (res + dfs(i+1, p2, pt+1)) % MOD
            for i in range(p2, n2):
                if word2[i] == target[pt]:
                    res = (res + dfs(p1, i+1, pt+1)) % MOD
            return res

        return dfs(0, 0, 0)
