class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals=[[1,100],[11,22],[1,11],[2,12]]
        #            [[1,11],[2,12],[11,22],[1,100]]
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        print(intervals)

        res = 0
        prev_end = intervals[0][1]


        for start,end in intervals[1:]:
            if start < prev_end:
                res += 1
            else:
                prev_end = end
        return res

        