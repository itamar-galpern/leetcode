class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged, i = [], 0
        while i < len(intervals):
            start, end = intervals[i]
            i += 1
            while i < len(intervals):
                next_start, next_end = intervals[i]
                if next_start <= end:
                    end = max(end, next_end)
                else:
                    break
                i+= 1
            merged.append([start, end])
        return merged

