class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        q = deque([0 for _ in range(26)])
        for k, v in Counter(s).items():
            q[ord(k) - 97] = v

        for _ in range(t):
            q.appendleft(q.pop())   # in each iteration, the counts are propagated rightwards, a -> b -> c -> ...
            q[1] = (q[1] + q[0]) % MOD  # count of z is propagated to b as well

        return sum(q) % MOD
