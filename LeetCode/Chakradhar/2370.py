class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)

        LIS = [0 for _ in range(26)]    # similar cncept to LIS, max string len ending at index i

        for i in range(n):
            pivot = ord(s[i]) - 97
            l = max(0, pivot - k)
            r = min(25, pivot + k)

            LIS[pivot] = 1 + max(LIS[l:r+1])

        return max(LIS)
