class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =  1 , max(piles)
        result = max(piles)

        while l <= r:
            pivot = ( l + r )// 2
            k = pivot
            time = 0
            for p in piles:
                time += math.ceil(p / k)
                if time > h:
                    l = pivot + 1
                    break
            else:
                r = pivot - 1
                result = min(result, k)
        return result
