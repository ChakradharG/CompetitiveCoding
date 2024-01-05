class RevLexStr:

    def __init__(self, string):
        self.string = string

    def __lt__(self, other):
        return self.string > other.string


class SORTracker:

    def __init__(self):
        self.above, self.below = [], []
        self.index = 0

    def add(self, name: str, score: int) -> None:
        if self.above and ((score > self.above[0][0]) or \
        (score == self.above[0][0] and name < self.above[0][1].string)):
            score, name = heapq.heappushpop(self.above, (score, RevLexStr(name)))
            heapq.heappush(self.below, (-score, name.string))
        else:
            heapq.heappush(self.below, (-score, name))

    def get(self) -> str:
        score, name = heapq.heappop(self.below)
        heapq.heappush(self.above, (-score, RevLexStr(name)))
        return name


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()