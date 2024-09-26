class Trie:
    def __init__(self):
        self.d = {}
        self.end = False
        self.cnt = 0
    def add(self, word):
        node = self
        for c in word:
            if c not in node.d:
                node.d[c] = Trie()
            node = node.d[c]
            node.cnt += 1
        node.end = True
    def calc(self, word):
        node, res = self, 0
        for c in word:
            if c not in node.d:
                break
            node = node.d[c]
            res += node.cnt
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)

        ans = []
        for word in words:
            ans.append(trie.calc(word))

        return ans
