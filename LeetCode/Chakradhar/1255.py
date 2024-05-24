class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        words = [Counter(word) for word in words]
        letters = Counter(letters)
        score = {chr(i+97): score[i] for i in range(26)}

        def dfs(i):
            if i == len(words):
                return 0

            total = dfs(i+1)

            if canTake(words[i]):
                total = max(total, take(words[i]) + dfs(i+1))
                restore(words[i])

            return total

        def canTake(word):
            for c, cnt in word.items():
                if letters[c] < cnt:
                    return False
            return True

        def take(word):
            cur = 0
            for c, cnt in word.items():
                letters[c] -= cnt
                cur += (cnt * score[c])
            return cur

        def restore(word):
            for c, cnt in word.items():
                letters[c] += cnt

        return dfs(0)