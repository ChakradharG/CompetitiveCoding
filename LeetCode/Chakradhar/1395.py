class BIT:
    def __init__(self, length):
        self.tree = [0 for _ in range(length)]  # <= i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

    def update(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += (i & -i)

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        mn, mx = min(rating), max(rating)
        ltbit, gtbit = BIT(mx - mn + 2), BIT(mx - mn + 2)

        smaller = []
        for j in range(n):
            smaller.append(ltbit.query(rating[j] - mn))
            ltbit.update(rating[j] - mn + 1)

        ans = 0
        for j in reversed(range(n)):
            ans += smaller[j] * ((n - j - 1) - gtbit.query(rating[j] - mn + 1))
            ans += (j - smaller[j]) * gtbit.query(rating[j] - mn)
            gtbit.update(rating[j] - mn + 1)

        return ans
