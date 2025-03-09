class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        d = defaultdict(set)
        for x, y in edges:
            d[x].add(y)
            d[y].add(x)
        
        if source not in d:
            return False
        

        
        visited = set()
        ans = False

        def dfs(node):
            nonlocal ans
            if ans or node in visited:
                return

            if node == destination:
                ans = True
                return
                
            visited.add(node)
            print(d[node])
            for x in d[node]:
                print(x)
                dfs(x)

        dfs(source)
        return ans

            


        
