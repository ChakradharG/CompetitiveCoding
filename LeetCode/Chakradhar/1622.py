class Fancy:

    def __init__(self):
        self.m, self.a = 1, 0
        self.l = []

    def append(self, val: int) -> None:
        self.l.append([val, self.m, self.a])

    def addAll(self, inc: int) -> None:
        self.a += inc

    def multAll(self, m: int) -> None:
        self.m *= m
        self.a *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.l):
            return -1
        x, alpha, beta = self.l[idx]
        alpha = self.m // alpha
        beta = self.a - (alpha*beta)
        return (alpha*x + beta) % MOD

MOD = 10**9 + 7
# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)