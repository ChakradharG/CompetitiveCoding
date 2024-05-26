class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        indices = []
        k -= 1
        for i in range(n-1, -1, -1):
            q, k = divmod(k, math.factorial(i))
            indices.append(q)

        seq = [str(i) for i in range(1, n+1)]
        ans = ''
        for i in indices:
            ans += seq[i]
            seq.pop(i)

        return ans
