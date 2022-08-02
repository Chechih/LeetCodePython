from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalsLeg = len(intervals)
        if intervalsLeg < 2:
            return intervals
        
        intervals = sorted(intervals, key = lambda li: li[0])
        mergeIntervals = [intervals[0]]

        for i in range(1, intervalsLeg):
            itv = intervals[i]
            first = itv[0]
            second = itv[1]
            previousItv = mergeIntervals.pop()
            previousFirst = previousItv[0]
            previousScond = previousItv[1]
            if previousScond >= first:
                mergeIntervals.append([previousFirst, max(second, previousScond)])
            else:
                mergeIntervals.append(previousItv)
                mergeIntervals.append(itv)
        return mergeIntervals
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.merge(intervals + [newInterval])