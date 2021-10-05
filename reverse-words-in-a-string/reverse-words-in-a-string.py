class Solution:
    def reverseWords(self, s: str) -> str:
        remove_extra_space = [i.strip() for i in s.split()]
        return ' '.join(remove_extra_space[::-1])   