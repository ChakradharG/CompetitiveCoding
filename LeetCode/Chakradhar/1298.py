class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # status: 0->nothing, 1->key, 2->box, 3->queued
        q = deque([])
        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
                status[box] = 3
            else:
                status[box] = 2

        ans = 0
        while q:
            box = q.popleft()
            ans += candies[box]
            for new in keys[box]:
                if status[new] == 2:
                    q.append(new)
                    status[new] = 3
                else:
                    status[new] = 1
            for new in containedBoxes[box]:
                if status[new] == 1:
                    q.append(new)
                    status[new] = 3
                else:
                    status[new] = 2

        return ans
