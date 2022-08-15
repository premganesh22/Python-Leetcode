class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        start = 0
        end = len(cardPoints)-k
        ksum = sum(cardPoints[end:])
        max_count = ksum
        
        for i in range(start,k):
            ksum= ksum - cardPoints[end] + cardPoints[start]
            max_count = max(max_count, ksum )
            start+=1
            end+=1
        return max_count
        