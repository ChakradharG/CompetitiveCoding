class Fancy:

    def __init__(self):
        self.m, self.a = 1, 0
        self.l = []

    def append(self, val: int) -> None:
        self.l.append([val, self.m, self.a])

    def addAll(self, inc: int) -> None:
        self.a += inc
        # if len(self.l) == 0:
        #     return
        # while len(self.ops) > self.l[-1][1] and self.ops[-1][0] == '+':
        #     inc += self.ops.pop()[1]
        # self.ops.append(['+', inc % MOD])

    def multAll(self, m: int) -> None:
        self.m *= m
        self.a *= m
        # if len(self.l) == 0:
        #     return
        # while len(self.ops) > self.l[-1][1] and self.ops[-1][0] == '*':
        #     m *= self.ops.pop()[1]
        # self.ops.append(['*', m % MOD])

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.l):
            return -1
        x, alpha, beta = self.l[idx]
        alpha = self.m // alpha
        beta = self.a - (alpha*beta)
        return (alpha*x + beta) % MOD
        # x, i = self.l[idx]
        # while i < len(self.ops):
        #     op, y = self.ops[i]
        #     if op == '+':
        #         x += y
        #     else:
        #         x = (x * y) % MOD
        #     i += 1
        # x %= MOD
        # self.l[idx] = [x, i]
        # return x

MOD = 10**9 + 7
# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)