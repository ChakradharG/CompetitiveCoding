row = [False] * (10**5+1) # row[i] indicates whether the player in play when
# `i` stones are remaining can win or not
for c in range(1, 10**5+1):
    row[c] = not row[c-1]
    i = math.floor(math.sqrt(c))
    i2 = i*i
    while i > 1 and not row[c]:
        row[c] = not row[c-i2]
        i2 -= (2*i - 1)
        i -= 1

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return row[n]
