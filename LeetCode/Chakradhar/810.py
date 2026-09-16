class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        s = 0
        for num in nums:
            s ^= num

        if s == 0:
            # alice wins by default
            return True

        # now starting s is non-zero, we can write this as s0 = 0 ^ s 
        # i.e., at least 1 element is non-zero. It is optimal to not pick
        # that 1 element and pick the rest. Now, if there are even elements
        # then bob is left with the last non-zero elem, hence alice wins.
        # otherwise, alice is the one left with the last elem, and bob wins
        return len(nums) % 2 == 0

