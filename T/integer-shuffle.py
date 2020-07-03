"""
This method takes an input integer and returns the shuffled representation
of that integer
Params: int
Return Type: int
"""
def solution1(A):
    # Cast to string in order to iterate through
    A = str(A)
    # Base case of recursion, when our length <= 2 we cannot shift further
    if len(A) <= 2:
        return int(A)

    # Here we build our result:
    # Append last digit to one digit ahead of first digit of CURRENT string
    # Then recurse, break down into substrings until bsae case is hit.
    return int((A[0] + A[-1]) + str(solution1(A[1:-1])))

# Without converting to string approach
# Approach, write as a linear combination of the two
def solution2(A):
    # Base case, when A is less than three digits
    if A < 100:
        return A
    # Need to truncate digit
    trunc = A
    # Running power
    power = 0
    while trunc > 0:
        trunc //= 10
        power += 1
        a = A // 10 ** (power-1) * 10 ** (power-1)
        b = (A % 10) * 10 ** (power-2)
        return a + b + solution2((A-a) // 10)

"""
Solution 1 Ex:
123456
16 + 2345
25 + 34
34 
--> 162534
"""


"""
Solution 2 ex: 
17272 --> 10000 + 2000    
727 --> 700 + 70
2 --> returned
10000 + 2000 + 700 + 70 + 2 = 12772

"""


