class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        ans = []

        
        for xj, yj, r in queries:
            count = 0
            
            for x, y in points:
            
                jarak_kuadrat = (xj - x) ** 2  + (yj - y) ** 2
            
                if jarak_kuadrat <= r ** 2:
                    count +=1

            ans.append(count)

        return ans