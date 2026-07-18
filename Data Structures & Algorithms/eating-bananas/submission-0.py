class Solution:
    """
    piles = [3,6,7,11] & h = 8
    piles[i] / k, where i= 0,1,2,3

    k: [1, max(piles)]
       = [1,2,3,4,5,6,7,8,9,10,11]

    Time: O(n * log(max(piles)))
    Space: O(1)
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h
        
        l, r = 1, max(piles)
        while l < r:
            k = (l+r) // 2
            if k_works(k):
                r = k
            else:
                l = k + 1 
        return r