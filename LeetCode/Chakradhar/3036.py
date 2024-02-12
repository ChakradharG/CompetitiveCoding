class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        l1, l2 = len(nums), len(pattern)

        for i in range(l1-1):
            x = (nums[i+1] - nums[i])
            if x > 0:
                nums[i] = 1
            elif x == 0:
                nums[i] = 0
            else:
                nums[i] = -1

        LPS = [0 for _ in range(l2)]
        p, c = 0, 1
        while c < l2:
            if pattern[p] == pattern[c]:
                LPS[c] = p + 1
                p, c = p + 1, c + 1
            else:
                if p == 0:
                    LPS[c] = 0
                    c += 1
                else:
                    p = LPS[p - 1]

        matches = 0
        h, n = 0, 0
        while h < l1:
            if nums[h] == pattern[n]:
                h, n = h + 1, n + 1
            else:
                if n == 0:
                    h += 1
                else:
                    n = LPS[n - 1]

            if n == l2:
                matches += 1
                n = LPS[n - 1]

        return matches
