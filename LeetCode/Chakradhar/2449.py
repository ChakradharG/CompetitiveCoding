class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        no, ne = [], []
        to, te = [], []
        for n, t in zip(nums, target):
            if n % 2:
                no.append(n)
            else:
                ne.append(n)
            if t % 2:
                to.append(t)
            else:
                te.append(t)
        no.sort()
        ne.sort()
        to.sort()
        te.sort()

        ans = 0
        for n, t in zip(no, to):
            ans += abs(n - t) // 2
        for n, t in zip(ne, te):
            ans += abs(n - t) // 2

        return ans // 2

