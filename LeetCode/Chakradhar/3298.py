class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        d = defaultdict(int)
        freq = Counter(word2)
        mtc = len(freq)
        l = r = ans = 0
        while r < n:
            d[word1[r]] += 1
            if d[word1[r]] == freq[word1[r]]:
                mtc -= 1
            while mtc == 0:
                ans += (n - r)
                if d[word1[l]] == freq[word1[l]]:
                    mtc += 1
                d[word1[l]] -= 1
                l += 1
            r += 1

        return ans

