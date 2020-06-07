class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for denom in coins:
            for i in range(1, amount+1):
                if i >= denom:
                    dp[i] += dp[i - denom]
        return dp[-1]
