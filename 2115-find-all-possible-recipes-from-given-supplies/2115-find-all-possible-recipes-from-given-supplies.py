class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    
        reci = {}
        for r in range(len(recipes)):
            reci[recipes[r]] = len(ingredients[r])
        

        ings = {}
        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                if ing in ings:
                    ings[ing].append(recipes[i])
                else:
                    ings[ing] = [recipes[i]]
                    
        ##Add all ings to queue
        q = deque()
        for item in supplies:
            print(item)
            q.append(item)
            
        ans = []
        while q:
            ingredient = q.popleft()
            if ingredient in ings:
                for receipe in ings[ingredient]:
                    reci[receipe]-=1
                    if reci[receipe] == 0:
                        ans.append(receipe)
                        q.append(receipe)
        return ans
        