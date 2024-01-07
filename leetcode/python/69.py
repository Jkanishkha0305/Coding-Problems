class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low<= high:
            mid = (low+high) // 2
            mid_sq = mid * mid
            
            if mid_sq < x:
                low = mid + 1
            elif mid_sq > x:
                high = mid - 1
            else:
                return mid
        return high