class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
    
        if len(matrix) == 0 or matrix == []:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        height = 0
        
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    height = max(height, dp[i][j])
        return height ** 2
