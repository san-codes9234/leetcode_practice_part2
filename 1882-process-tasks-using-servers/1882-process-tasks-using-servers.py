import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []

        ans = []
        t = 0

        for j, duration in enumerate(tasks):
            t = max(t, j)

            if not free:
                t = max(t, busy[0][0])

            while busy and busy[0][0] <= t:
                ft, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            w, idx = heapq.heappop(free)
            ans.append(idx)
            heapq.heappush(busy, (t + duration, w, idx))

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
