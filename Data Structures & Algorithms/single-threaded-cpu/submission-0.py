import heapq
class Task:
    def __init__(self, enq_time, duration):
        self.enq_time = enq_time
        self.duration = duration
    
    def __lt__(self, b):
        return self.duration < b.duration

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_map = {}
        for i,t in enumerate(tasks):
            task_map[tuple(t)] = i
        tasks.sort()
        cursor = 0
        time = tasks[0][0]
        heap = []
        res = []
        while heap or cursor < len(tasks):
            while cursor < len(tasks) and tasks[cursor][0] <= time:
                task = Task(tasks[cursor][0],tasks[cursor][1])
                heapq.heappush(heap, task)
                cursor += 1
            
            if heap: 
                task = heapq.heappop(heap)
                res.append([task.enq_time, task.duration])
                time += task.duration
            else:
                time += 1
        
        return [task_map[tuple(d)] for d in res]

            
