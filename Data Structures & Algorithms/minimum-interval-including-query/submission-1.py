from _heapq import heapreplace
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_idx = [[q,i] for i,q in enumerate(queries)]        
        intervals.sort()
        queries_idx.sort()
        res = []
        heap = []
        idx = 0
        for q,i in queries_idx:
            while idx < len(intervals) and intervals[idx][0] <= q:
                l,r = intervals[idx]
                heapq.heappush(heap, (r-l+1, r))
                idx += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if not heap:
                res.append((i,-1))
            else:
                res.append((i,heap[0][0]))

            
        return [m for _,m in sorted(res)]
