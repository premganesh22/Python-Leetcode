class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        buffer_word = []
        ans = ''
        word_count = 0
        max_val = 0

        dic = defaultdict(int)
        for p,char in enumerate(paragraph):
            if char.isalnum():
                buffer_word.append(char.lower())
                if p != len(paragraph)-1:
                    continue
            if len(buffer_word) > 0:
                word = ''.join(buffer_word)
            if word not in banned:
                dic[word]+=1
                if dic[word] > max_val:
                    max_val = dic[word]
                    ans = word
            buffer_word = []
        return ans
        
        