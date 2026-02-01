class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = defaultdict(list)
        deg = defaultdict(int)
        mp = {}
        for i, r in enumerate(recipes):
            for ing in ingredients[i]:
                g[ing].append(r)
                deg[r] += 1
            mp[r] = i

        canMake = [False] * len(recipes)

        q = deque(supplies)

        while q:
            ing = q.popleft()
            if ing in mp:
                canMake[mp[ing]] = True
            for nei in g[ing]:
                deg[nei] -= 1
                if not deg[nei]:
                    q.append(nei)

        return [recipes[i] for i, x in enumerate(canMake) if x == True]

        