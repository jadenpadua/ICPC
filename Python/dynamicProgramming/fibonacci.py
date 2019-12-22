# TC: O(2^n) time and O(n) space, naive solution of brute force recursion
def getNthFib1(n):
    # Base cases for first and second fib number
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        # Apply fib formula, straight forward
        return getNthFib1(n - 1) + getNthFib1(n - 2)

# Dynamic programming approach, store memoized solutions in a hashtable so we don't need to re call
def getNthFib2(n, memoize={1:0, 2:1}): # init our ht and provide the base cases
    # if already in our ht, just return the value, do not need to recurse deeper
    if n in memoize:
        return memoize[n]
    # else create new memoize solution in ht and recurse deeper
    else:
        memoize[n] = getNthFib2(n-1,memoize) + getNthFib2(n-2, memoize)
        # Will keep going until hits our two defined base cases
        return memoize[n]

# Upgraded approach to omit extra space, we only need space of the last two fib numbers
# O(n) time | O(1) space
def getNthFib3(n):
    #starting our base cases, mapping lastTwo[0] to first fib num and lastTwo[1] to second fib num
    lastTwo = [0,1]
    counter = 3 # init our counter, used to get to our number n
    while counter <= n: # while our counter has  not reached our n passed in
        nextFib = lastTwo[0] + lastTwo[1] # now add the two nums in array, that will be our next fib
        lastTwo[0] = lastTwo[1] # now update positions in array
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0] # now return last array position, HOWEVER if n is <= 1, we must return 0
print(getNthFib1(6))
print(getNthFib2(6))
print(getNthFib3(6))
