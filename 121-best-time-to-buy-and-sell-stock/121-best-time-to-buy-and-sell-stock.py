class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_max = 0
        prev_min = prices[0]
        
        for price in range(1, len(prices)):
            
            if prices[price]-prev_min > global_max:
                global_max = prices[price]-prev_min
            
            prev_min = min(prev_min, prices[price])
        return global_max
        