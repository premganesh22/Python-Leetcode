class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        output = [float('inf')]*(amount+1)
        output[0] = 0
        
        for val in range(1,amount+1):
            find_min = float('inf')
            for coin in coins:
                if val-coin>=0:
                    find_min = min(output[val-coin],find_min)
                    
            output[val] = find_min+1
        if output[amount] == float('inf'):
            return -1
        return output[amount]

#         Recusion
#         global_count = [float('inf')]
#         def change(money,step):
#             #print(money,step)
#             if money<0:
#                 return
#             if money == 0:
#                 global_count[0] = min(step,global_count[0])
#                 return
#             for coin in coins:
#                 change(money-coin,step+1)
                
#         change(amount,0)
#         return global_count[0] if global_count[0] < float('inf') else -1