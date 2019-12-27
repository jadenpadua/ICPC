# Given an int value representing a target amount, and an array of coin denoms,
# Find min number of coins out of coins we are given to reach target amount
# Assume an infinite amount of coin denoms

# Idea: Using dynamic programming here, create an index of number from 0 to n
# now build out memoized array one denom at a time,
# Runs in O(nd) time and O(n) space
def minNumberOfCoinsForChange(n,denoms):
    # fille with greatest value so we can overwrite later with min values
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0 #base case, to make 0 dollars we need 0 coins
    # iterate through all our denoms
    for denom in denoms:
        # now iterate through our nom coins memoized array for each denom
        for amount in range(len(numOfCoins)):
            # if our denom is less than amount it means possible coin exhange
            if denom <= amount:
                # now update this amount index to reflect the min of numCoins[amount], 
                # 1 + numOfCoins[amount - denom], reflects the one coin we are adding 
                # plus the numOfCoins[amount - denom], so for example for amount of 6
                # min(numcoins[6], 1 + numCoins[ 6 - 2])
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
            # return last index of num coins
            return numOfCoins[n] if numOfCoins[n] != float("inf") else -1
