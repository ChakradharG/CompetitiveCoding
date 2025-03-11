class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        d, need, cons = defaultdict(int), 5, 0
        vowels = set('aeiou')

        ans = 0
        l, g, r = 0, 0, 0
        while r < n:
            if word[r] in vowels:
                d[word[r]] += 1
                if d[word[r]] == 1:
                    need -= 1
                while d[word[g]] > 1:
                    d[word[g]] -= 1
                    g += 1
            else:
                cons += 1
                while cons > k:
                    if word[l] not in vowels:
                        cons -= 1
                    l += 1
                while g < l:
                    d[word[g]] -= 1
                    if d[word[g]] == 0:
                        need += 1
                    g += 1
                while g < r and d[word[g]] > 1:
                    d[word[g]] -= 1
                    g += 1
            if need == 0 and cons == k:
                ans += (g - l + 1)

            r += 1

        return ans
