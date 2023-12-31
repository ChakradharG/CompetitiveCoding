class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        winLen = wordLen * len(words)
        wordsD = defaultdict(int)
        for word in words:
            wordsD[word] += 1

        if len(s) < winLen:
            return []

        idxs = []
        for i in range(wordLen):
            l, r = i, i
            wordsCopy = wordsD.copy()
            while r < len(s):
                word = s[r:r+wordLen]
                if wordsCopy[word] > 0:
                    wordsCopy[word] -= 1
                    r += wordLen
                else:
                    if l == r:
                        r += wordLen
                        l = r
                    else:
                        wordsCopy[s[l:l+wordLen]] += 1
                        l += wordLen

                if (r - l) == winLen:
                    idxs.append(l)
                    wordsCopy[s[l:l+wordLen]] += 1
                    l += wordLen

                if l > (len(s) - winLen):
                    break

        return idxs
