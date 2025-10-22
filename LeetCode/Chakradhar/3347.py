class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if k == 0 or numOperations == 0:
            return sorted(Counter(nums).items(), reverse=True, key=lambda x: x[1])[0][1]

        h = []
        for num in nums:
            h.append((num+k+1, 0))
            h.append((num+1, 1))
            h.append((num-k, 2))
            h.append((num, 3))
        h.sort()

        c, e = 0, 0
        ans = 0
        for v, d in h:
            if d == 0:
                c -= 1
            elif d == 1:
                e -= 1
            elif d == 2:
                c += 1
            else:
                e += 1
            ans = max(ans, e + min(numOperations, c-e))

        return ans
