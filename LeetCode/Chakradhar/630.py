class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])    # sort by deadline
        heap = []   # max heap
        cnt, t = 0, 0

        for (d, l) in courses:
            if (t + d) <= l:
                # can take current course
                cnt += 1
                t += d
                heapq.heappush(heap, -d)
            elif heap and (-heap[0] > d) and (t + d + heap[0]) <= l:
                # if there is an already taken course
                # that is shorter than the current course
                # and we can take the current course before its deadline if we skip that previous courses
                # unlearn previous course and take current course
                t += heapq.heappop(heap)
                t += d
                heapq.heappush(heap, -d)

        return cnt
