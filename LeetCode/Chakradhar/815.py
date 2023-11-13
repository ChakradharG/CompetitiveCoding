class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        connectedBuses = {}
        busesOnStop = {}
        for bus, route in enumerate(routes):
            for stop in route:
                if stop in busesOnStop:
                    for bus2 in busesOnStop[stop]:
                        if bus not in connectedBuses:
                            connectedBuses[bus] = set()
                        if bus2 not in connectedBuses:
                            connectedBuses[bus2] = set()
                        connectedBuses[bus].add(bus2)
                        connectedBuses[bus2].add(bus)
                    busesOnStop[stop].append(bus)
                else:
                    busesOnStop[stop] = [bus]

        if source == target:
            return 0
        elif target not in busesOnStop:
            return -1
        targetBuses = set(busesOnStop[target])

        cnt = 1
        visited, q = set(), deque(busesOnStop[source])
        while q:
            for i in range(len(q)):
                bus = q.popleft()
                visited.add(bus)
                if bus in targetBuses:
                    return cnt
                for bus2 in connectedBuses.get(bus, []):
                    if bus2 not in visited:
                        q.append(bus2)
            cnt += 1

        return -1
