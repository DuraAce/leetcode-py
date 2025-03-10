class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n 

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return

            for c in phone_dict[digits[i]]:
                path[i] = c
                dfs(i+1)
        
        dfs(0)
        return ans
