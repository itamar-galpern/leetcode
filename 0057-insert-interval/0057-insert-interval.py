class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        return_arr = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                return_arr.append(newInterval)
                return return_arr + intervals[i:]
            elif newInterval[0] > interval[1]:
                return_arr.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        return return_arr + [newInterval]
        