import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((enq, dur, idx) for idx, (enq, dur) in enumerate(tasks))
        time = tasks[0][0]
        heap = []
        cursor = 0
        res = []
        print(tasks)
        while heap or cursor < len(tasks):
            while cursor < len(tasks) and tasks[cursor][0] <= time:
                _,dur,idx = tasks[cursor]
                heapq.heappush(heap, (dur, idx))
                cursor += 1

            if heap:
                dur,idx = heapq.heappop(heap)
                res.append(idx)
                time += dur
            elif time < tasks[cursor][0]:
                time = tasks[cursor][0]
        
        return res
