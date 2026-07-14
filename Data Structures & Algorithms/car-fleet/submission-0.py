class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speeds = {}
        for p,s in zip(position, speed):
            speeds[p] = s
        
        position.sort()
        
        time = []
        for p in position:
            time.append((target - p)/speeds[p])
        
        stack = []
        for t in time[::-1]:
            if not stack or stack[-1] < t:
                stack.append(t)
        
        return len(stack)


