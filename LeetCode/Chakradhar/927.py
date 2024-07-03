class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = arr.count(1)
        if ones % 3 != 0:   # each value should have equal number of 1s
            return [-1, -1]
        elif ones == 0:
            return [0, len(arr) - 1]

        ones //= 3
        cnt = 0
        # [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1]
        # [      1  2     3     1  2  3           1        2  3]
        # [               p1    p2    p3          p4           ]
        p1 = p2 = p3 = p4 = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 1:
                cnt += 1
                if cnt == ones:
                    p4 = i
                if cnt == ones + 1:
                    p3 = i
                if cnt == (2 * ones):
                    p2 = i
                if cnt == (2 * ones + 1):
                    p1 = i

        v3 = 0  # rightmost value, this is fixed (can only have leading 0s)
        for i in range(p4, len(arr)):
            v3 = (v3 << 1) + arr[i]
        v2 = 0  # middle value, can add 0s on both ends
        for i in range(p2, p3+1):
            v2 = (v2 << 1) + arr[i]
        v1 = 0  # leftmost value, can only append 0s (multiply by 2)
        for i in range(0, p1+1):
            v1 = (v1 << 1) + arr[i]

        z2 = p4 - p3 - 1    # number of 0s b/w p3 and p4
        while z2 > 0 and v2 < v3:
            z2 -= 1
            v2 *= 2
        if v2 != v3:
            return [-1, -1]
        else:
            # append the required number 0s to v2, the rest are leading 0s in v3
            a2 = p4 - z2    # start index of v3

        z1 = p2 - p1 - 1    # number of 0s b/w p1 and p2
        while z1 > 0 and v1 < v2:
            z1 -= 1
            v1 *= 2
        if v1 != v2:
            return [-1, -1]
        else:
            # append the required number 0s to v1, the rest are leading 0s in v2
            a1 = p2 - z1 - 1    # end index of v1

        return [a1, a2]
