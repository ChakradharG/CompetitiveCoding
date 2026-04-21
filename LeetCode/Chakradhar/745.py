class Trie:
    def __init__(self):
        self.d = {}
        self.idx = -1
    def add(self, i, word):
        node = self
        for c in word:
            if c not in node.d:
                node.d[c] = Trie()
            node = node.d[c]
            node.idx = max(node.idx, i)
    def search(self, word):
        node = self
        for c in word:
            if c not in node.d:
                return -1
            node = node.d[c]
        return node.idx

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, word in enumerate(words):
            pref = word
            for j in range(len(word)):
                self.trie.add(i, f"{word[j:]}[{pref}")

    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(f"{suff}[{pref}")
