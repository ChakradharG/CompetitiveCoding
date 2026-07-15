class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        @cache
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n, m = len(nums), max(nums) + 1
        MOD = 10**9 + 7
        grid = [[1 if i==j else 0 for j in range(m)] for i in range(m)]
        grid[0][0] = 0

        poss = [[]]
        prv = set()
        for num in nums:
            cur = {num}
            for x in prv:
                cur.add(gcd(num, x))
            prv |= cur
            poss.append(sorted(prv))

        for i in reversed(range(n)):
            num, p = nums[i], poss[i]
            grid[0][0] = (grid[0][0] + grid[num][0] + grid[0][num]) % MOD
            for seq1 in reversed(p):
                y = seq1
                grid[y][0] = (grid[y][0] + grid[gcd(y, num)][0] + grid[y][num]) % MOD
                grid[0][y] = (grid[0][y] + grid[num][y] + grid[0][gcd(y, num)]) % MOD
            for seq1 in reversed(p):
                for seq2 in reversed(p):
                    grid[seq1][seq2] = (
                        grid[seq1][seq2]
                        + grid[gcd(seq1, num)][seq2]
                        + grid[seq1][gcd(seq2, num)]
                    ) % MOD

        return grid[0][0]
