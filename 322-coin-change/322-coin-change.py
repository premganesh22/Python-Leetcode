class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
     

        table = [-1]*(amount+1)
        table[0] = 0
        for i in range(1, len(table[1:])+1):
            min_val = float('inf')
            for coin in coins:
                if i-coin >= 0 and table[i-coin] != -1:
                    min_val = min(min_val,table[i-coin])
            table[i] = min_val+1 if min_val != float('inf') else -1
        return table[amount]
        