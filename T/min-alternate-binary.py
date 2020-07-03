import unittest
"""
This method takes in a bit integer of 0/1 and flips it respectively
Params: int
Return Type: int
"""


def alternate(bit):
    # Simple ternary that flips the bit based on input
    return 1 if (bit == 0) else 0


"""
This method returns the minimum number of flips that the array needs in order
to achieve total alternation:
Params: (List[int], int)
Return Type: int
"""


def getMinFlips(A, expected):
    # Minimum flip counter
    count = 0
    # Iterate through binary array
    for i in range(len(A)):
        # Count increases if character is not in alternation order (If expected value does not match)
        if A[i] != expected:
            count += 1
        # Now update the expected value into its alternate bit
        expected = alternate(expected)
    # Return minimum flip counter
    return count


"""
Driver method returns the minimum flip number for alternation of BOTH cases:
Arrays with a starting index of 0 AND Arrays with a starting index of 1
Params: (List[int])
Return Type: int
"""


def solution(A):
    # Two options we must consider: Either alternative binary i starting at 0 or one
    # Of these two options, we will take the minimum of the two
    return min(getMinFlips(A,0), getMinFlips(A,1))


class testSolution(unittest.TestCase):
    def test_basic(self):
        self.assertEquals(solution([1,0,0,0]), 1)

if __name__ == '__main__':
    unittest.main()
