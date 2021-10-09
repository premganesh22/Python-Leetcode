class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        index = 0
        for i in range(len(chars)):
            if i < len(chars)-1 and chars[i] == chars[i+1]:
                count+=1
            else:
                if count > 1:
                    chars[index] = chars[i]
                    index+=1
                    for num in str(count):
                        chars[index] = num
                        index+=1
                else:
                    chars[index] = chars[i]
                    index = index+1
                count = 1
        return index