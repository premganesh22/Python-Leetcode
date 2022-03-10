class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def phone(digits,digit_idx,slate,result):
            if digit_idx == len(digits):
                result.append(''.join(slate))
                return
            else:
                string = dic[digits[digit_idx]]
                for i in range(len(string)):
                    slate.append(string[i])
                    phone(digits,digit_idx+1,slate,result)
                    slate.pop()
                return result
        return phone(digits,0,[],[])
            
                    
                    