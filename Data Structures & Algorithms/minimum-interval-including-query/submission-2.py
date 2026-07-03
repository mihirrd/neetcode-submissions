from _heapq import heapreplace
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        heap = []
        idx = 0
        for q in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= q:
                l,r = intervals[idx]
                heapq.heappush(heap, (r-l+1, r))
                idx += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)            
        
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]
