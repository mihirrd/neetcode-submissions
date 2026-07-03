class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_idx = [[q,i] for i,q in enumerate(queries)]
        queries_idx.sort()
        idx = 0
        res = []
        for q,i in queries_idx:
            min_diff = float("inf")
            idx = 0
            while idx < len(intervals):
                l,r = intervals[idx]
                if l <= q <= r:
                    min_diff = min(min_diff, r - l + 1)
                idx += 1
            min_diff = min_diff if min_diff != float("inf") else -1
            res.append((i,min_diff))
        return [m for _,m in sorted(res)]
