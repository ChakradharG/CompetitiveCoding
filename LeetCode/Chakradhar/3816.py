class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        comp = []
        occ = defaultdict(int)
        cur, l = s[0], 1
        for c in s[1:] + '#':
            if c != cur:
                occ[cur] += 1
                comp.append((cur, l, occ[cur]))
                cur, l = c, 0
            l += 1

        stack = []
        final = []
        inFinal = set()
        for c, l, o in comp:
            while stack and stack[-1][0] > c:
                c2, l2, o2 = stack.pop()
                if o2 == occ[c2] and (c2 not in inFinal):
                    for c3, l3, o3 in stack:
                        final.append((c3, l3, o3))
                        inFinal.add(c3)
                    final.append((c2, 1, o2)) 
                    stack = []
            if stack and stack[-1][0] == c:
                stack[-1] = (c, stack[-1][1]+l, o)
            else:
                stack.append((c, l, o))

        st = []
        for c, l, o in stack:
            if not st or st[-1][0] != c:
                st.append((c, l, o))
            else:
                st[-1] = c, st[-1][1]+l, st[-1][2]
        stack = st

        while stack:
            c, l, o = stack.pop()
            if c not in inFinal:
                stack.append((c, 1, o))
                break

        return ''.join([c*l for c, l, _ in (final + stack)])
