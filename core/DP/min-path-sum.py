class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        # dp array to solve smaller sub problems
        dp = [[0 for value in row] for row in grid]
        
        # solve sub problems
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                dp[i][j] += grid[i][j]
                # must come from above and to the left
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j],dp[i][j-1])
                # if not on 0th row
                elif i > 0:
                    dp[i][j] += dp[i-1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j-1]
                    
        
        return dp[len(dp)-1][len(dp[0]) - 1]
