import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            candidate = (distance, point)
            if len(heap) < k:
                heapq.heappush_max(heap, candidate)
            else:
                heapq.heappushpop_max(heap, candidate)
        return [heap[i][1] for i in range(k)]
        
        