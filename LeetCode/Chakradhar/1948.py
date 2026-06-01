class Trie:
    def __init__(self) -> None:
        self.d = {}
        self.i = -1
        self.h = ""
    def add(self, path: List[str], idx: int) -> None:
        node = self
        for p in path:
            if p not in node.d:
                node.d[p] = Trie()
            node = node.d[p]
        node.i = idx

class Solution:
    def computeHash(self, node: Trie) -> str:
        for k in sorted(node.d.keys()):
            node.h += f"({k},{self.computeHash(node.d[k])})#"
        if len(node.h) > 0:
            self.freq[node.h] += 1
        return node.h
    def traverse(self, node: Trie) -> None:
        if node.i > -1:
            if self.freq[node.h] > 1:
                return
            self.unique.append(node.i)
        for v in node.d.values():
            self.traverse(v)
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = Trie()
        for i, path in enumerate(paths):
            trie.add(path, i)

        self.freq = defaultdict(int)
        self.computeHash(trie)

        self.unique = []
        self.traverse(trie)

        return [paths[i] for i in self.unique]
