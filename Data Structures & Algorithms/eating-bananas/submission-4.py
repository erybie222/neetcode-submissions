class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =  1 , max(piles)
        result = r

        while l <= r:
            k = ( l + r )// 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)
                if time > h:
                    l = k + 1
                    break
            else:
                r = k - 1
                result = min(result, k)
        return result
