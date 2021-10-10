class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                let.append(log)
        # print(let)
        let.sort(key = lambda x:x.split()[0])
        # print(let)
        let.sort(key = lambda x:x.split()[1:])
        print(let+dig)
        return let+dig