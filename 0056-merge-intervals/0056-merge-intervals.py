class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged, i = [], 0
        while i < len(intervals):
            start, end = intervals[i]
            i += 1
            while i < len(intervals):
                curr_s, curr_e = intervals[i]
                if curr_s <= end:
                    if curr_e > end:
                        end = curr_e
                else:
                    break
                i+= 1
            merged.append([start, end])
        return merged

