class Trie:
    def __init__(self):
        self.d = {}
        self.end = False

    def add(self, word):
        node = self
        for c in word:
            if c not in node.d:
                node.d[c] = Trie()
            node = node.d[c]
        node.end = True

    def search(self, word):
        node = self
        for c in word:
            if c not in node.d:
                return False
            node = node.d[c]
            if node.end:
                return True
        return node.end

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        mx = 0
        for word in words:
            mx = max(mx, len(word))
            self.trie.add(word[::-1])

        self.q = deque(list('#' * mx))

    def query(self, letter: str) -> bool:
        self.q.pop()
        self.q.appendleft(letter)
        return self.trie.search(self.q)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)