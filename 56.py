from typing import List 


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda intervals: intervals[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

        return merged
    

sol = Solution()

intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals1)) #Expected Output : [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1,4],[4,5]]
print(sol.merge(intervals2)) #Expected Output : [[1, 5]]