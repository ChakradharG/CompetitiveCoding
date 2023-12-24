class TrieNode:
    def __init__(self):
        self.desc = {}
        self.end = False

    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.desc:
                node.desc[c] = TrieNode()
            node = node.desc[c]
        node.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.addWord(word)

        def dfs(i, j, node, curStr):
            inbounds = (0 <= i < m and 0 <= j < n)
            if not inbounds or \
            (i, j) in visited or \
            board[i][j] not in node.desc:
                return

            node = node.desc[board[i][j]]
            curStr += board[i][j]

            if node.end:
                ans.add(curStr)

            visited.add((i, j))
            dfs(i-1, j, node, curStr)
            dfs(i, j-1, node, curStr)
            dfs(i, j+1, node, curStr)
            dfs(i+1, j, node, curStr)
            visited.remove((i, j))

        m, n = len(board), len(board[0])
        visited = set()
        ans = set()

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, '')

        return ans
