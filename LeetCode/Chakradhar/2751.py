class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []

        for p, h, d, i in robots:
            if d == 'R':    # won't collide with the ones to its left
                stack.append((p, h, d, i))
            else:   # will collide with ones to its left and moving right
                while stack and stack[-1][2] == 'R':
                    p2, h2, d2, i2 = stack.pop()
                    if h > h2:
                        h -= 1
                    else:
                        if h < h2:
                            stack.append((p2, h2-1, d2, i2))
                        break
                else:
                    stack.append((p, h, d, i))

        return list(map(lambda x: x[1], sorted(stack, key=lambda x: x[3]))) # re-sorting in original order
