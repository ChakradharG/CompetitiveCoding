class TrieNode:
    def __init__(self):
        self.d = {}
        self.ids = (math.inf, 0)
    def add(self, word, l, idx):
        node = self
        for c in word:
            if c not in node.d:
                node.d[c] = TrieNode()
            node = node.d[c]
            if l < node.ids[0]:
                node.ids = (l, idx)
            elif l == node.ids[0] and idx < node.ids[1]:
                node.ids = (l, idx)
    def search(self, word):
        node = self
        for c in word:
            if c not in node.d:
                return node.ids[1]
            node = node.d[c]
        return node.ids[1]

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = TrieNode()
        sml = (math.inf, -1)
        for i, word in enumerate(wordsContainer):
            l = len(word)
            trie.add(word[::-1], l, i)
            if l < sml[0]:
                sml = (l, i)
        trie.ids = sml

        answer = []
        for word in wordsQuery:
            answer.append(trie.search(word[::-1]))

        return answer
