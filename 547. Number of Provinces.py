# BFS Solution
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # BFS find connected cities
        # Keep record of visited
        # iterate row
        visited = set()
        ans = 0
        n = len(isConnected)
        for i, x in enumerate(isConnected):
            if x[i] == 1 and i not in visited:
                ans += 1
                self.bfs(isConnected, visited, i)
        return ans

    
    def bfs(self, isConnected, visited, i):
        dq = deque([i])
        while dq:
            curr = dq.popleft()
            visited.add(curr)
            for j, x in enumerate(isConnected[curr]):
                if x == 1 and j not in visited:
                    dq.append(j)
                    has_connection = True


