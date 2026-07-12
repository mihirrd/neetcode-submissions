class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)

        def get_time(piles, speed):
            hours_spent = 0
            for b in piles:
                hours_spent += math.ceil(b/speed)
            return hours_spent

        ans = max(piles)
        while l <= r:
            m_speed = (l + r)//2        
            if get_time(piles, m_speed) >  h:
                l = m_speed + 1
            else:
                ans = m_speed
                r = m_speed - 1
        
        return ans
        