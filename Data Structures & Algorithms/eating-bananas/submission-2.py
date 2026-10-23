class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_range = range(1, max(piles) + 1)
        l, r =  0 , len(k_range) -1
        result = max(piles)

        while l <= r:
            pivot = ( l + r )// 2
            k = k_range[pivot]
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
