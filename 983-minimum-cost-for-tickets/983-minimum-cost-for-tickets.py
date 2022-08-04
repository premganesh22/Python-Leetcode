class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        total = [0]*len(days)
        total[0] = min(cost)

        def test(days):
            for n in range(1, len(days)):

                #case 1
                case1 = total[n-1] + cost[0]

                #case 2
                j = n
                while j >= 0  and days[n]-7 < days[j]:
                    j-=1

                if j >= 0:
                    case2 = total[j] + cost[1]
                else:
                    case2 = cost[1]

                #case 3
                j = n
                while j >= 0  and days[n]-30 < days[j]:
                    j-=1

                if j >= 0:
                    case3 = total[j] + cost[2]
                else:
                    case3 = cost[2]

                total[n] = min(case1, case2, case3)

            #return total
        test(days)
        return total[-1]