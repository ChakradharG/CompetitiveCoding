class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if not stations:
            return -1

        stations.append([target, 0])
        fuel = startFuel
        used, avail = [], []
        prev = 0
        for p, df in stations:
            fuel -= (p - prev)
            prev = p
            while fuel < 0 and avail:
                f = -heappop(avail)
                fuel += f
                heappush(used, f)
            if fuel < 0:
                break
            heappush(avail, -df)


        if fuel < 0:
            return -1
        return len(used)
