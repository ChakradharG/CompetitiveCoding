class Trie:
    def __init__(self):
        self.d = defaultdict(Trie)
        self.end = False
    def add(self, word):
        node = self
        for c in word:
            node = node.d[c]
        node.end = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        @cache
        def search(word, i):
            n = len(word)
            if i == n:
                return True
            node = trie
            while i < n:
                if node.end and search(word, i):
                    return True
                c = word[i]
                if c not in node.d:
                    return False
                node = node.d[c]
                i += 1
            return node.end

        words.sort()
        words.sort(key=len)
        ans = []
        trie = Trie()
        for word in words:
            if search(word, 0):
                ans.append(word)
            trie.add(word)

        return ans
