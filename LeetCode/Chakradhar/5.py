class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i+1, j-1

        maxLen = 0
        l, r = 0, 0
        for i in range(len(s)):
            t1, t2 = expand(i, i)
            if maxLen < (t2 - t1 + 1):
                maxLen = (t2 - t1 + 1)
                l, r = t1, t2
            t1, t2 = expand(i, i+1)
            if maxLen < (t2 - t1 + 1):
                maxLen = (t2 - t1 + 1)
                l, r = t1, t2

        return s[l:r+1]
