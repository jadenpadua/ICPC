# Function that takes in a coin number n and a list of denoms
# Function should return num ways to make change given these
# O(nd) time | where n is the target amount and d is num of denoms | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    # initial population of our ways memoized array
    # The index of ways stands for all numbers leading to n
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1 # base case that kicks off DP, at ways[0] there is only one way to make change
    # now run through every denom in our denoms list
    for denom in denoms:
        # Now we need to iterate through our ways array for each denom
        for amount in range(1, n + 1):
            # Checks if our current denom is less than amount in our memoized array
            # if it is less than that means we have to start updating the indexes
            # of our memized array since this now turns into a possible way to make change
            # For example, if denom is 5 and amount is 6, ways[6] = ways[6] + ways[1]
            if denom <= amount:
                # adding whatever current num of ways is plus current number of ways to geerate that
                # amount minus our given denomination
                ways[amount] = ways[amount] + ways[amount - denom]
    # return our last ways amount which is ways[n]
    return ways[n]
