class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(k):
            if k == 0:
                return 'a', -1
            x = math.floor(math.log2(k))
            y = k - 2**x
            c, i = dfs(y)
            if operations[x] == 0:
                return c, x
            else:
                return chr(((ord(c) - 97 + 1) % 26) + 97), x

        return dfs(k-1)[0]
