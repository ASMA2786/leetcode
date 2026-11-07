import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = []
        busy = []
        res = []

        for i in range(len(servers)):
            heapq.heappush(available, (servers[i], i))

        time = 0

        for i in range(len(tasks)):
            time = max(time, i)

            # Move free servers to available heap
            while busy and busy[0][0] <= time:
                end, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, jump to next free time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select server with minimum weight and index
            weight, index = heapq.heappop(available)

            res.append(index)

            # Server becomes free after processing the task
            heapq.heappush(busy, (time + tasks[i], weight, index))

        return res