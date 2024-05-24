class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def isEnqueued(board):
            flat = (tuple(board[0]), tuple(board[1]))
            return flat in enqueued

        def enqueue(board, zeroPos):
            flat = (tuple(board[0]), tuple(board[1]))
            enqueued.add(flat)
            q.append((board, zeroPos))

        def getZeroPos(board):
            for i in range(2):
                for j in range(3):
                    if board[i][j] == 0:
                        return (i, j)

        neighbors = {
            (0, 0): [(0, 1), (1, 0)],
            (0, 1): [(0, 0), (0, 2), (1, 1)],
            (0, 2): [(0, 1), (1, 2)],
            (1, 0): [(0, 0), (1, 1)],
            (1, 1): [(1, 0), (0, 1), (1, 2)],
            (1, 2): [(1, 1), (0, 2)]
        }

        target = [
            [1, 2, 3],
            [4, 5, 0]
        ]
        q = deque()
        enqueued = set()
        enqueue(board, getZeroPos(board))

        d = 0
        while q:
            for _ in range(len(q)):
                cur, (i, j) = q.popleft()
                if cur == target:
                    return d
                for (i1, j1) in neighbors[(i, j)]:
                    newb = deepcopy(cur)
                    newb[i][j], newb[i1][j1] = newb[i1][j1], newb[i][j]
                    if not isEnqueued(newb):
                        enqueue(newb, (i1, j1))
            d += 1

        return -1
