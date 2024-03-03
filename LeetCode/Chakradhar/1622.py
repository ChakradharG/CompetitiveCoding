class Fancy:

    def __init__(self):
        self.m, self.a = 1, 0
        self.l = []

    def append(self, val: int) -> None:
        # `pow` is computing modular inverse
        self.l.append((val - self.a) * pow(self.m, -1, MOD))

    def addAll(self, inc: int) -> None:
        self.a = (self.a + inc) % MOD

    def multAll(self, m: int) -> None:
        self.m = (self.m * m) % MOD
        self.a = (self.a * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.l):
            return -1
        return ((self.m * self.l[idx]) + self.a) % MOD

MOD = 10**9 + 7
# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)