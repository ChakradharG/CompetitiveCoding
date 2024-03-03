class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        zer, one = 0, 0
        # to get rid of zero at LSB is 1 operation: division
        # to get rid of one at LSB is 2 operations: sub + div
        #   (except the last most significant one, which only need 1 op)
        while num:
            if num & 0b1:
                one += 1
            else:
                zer += 1
            num >>= 1

        return zer + (2*one - 1)
