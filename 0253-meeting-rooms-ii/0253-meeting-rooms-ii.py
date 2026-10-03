import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        heap = []
        for start, end in intervals:
            if heap and start >= heap[0]:
                heapq.heappushpop(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)
        