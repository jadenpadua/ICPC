"""
This method takes in an uppercase string and returns the max move number
for a valid "BALLOON" string
Params: str
Return Type: int
"""
def solution(S):
    # Dictionary to count instances of BALLOON letters in string S
    freq = {'B': 0, 'A': 0, 'L': 0, 'O': 0, 'N': 0}
    # Iterate through string
    for char in S:
        # Enumerate dictionary if respective char is in string
        if char in freq:
            freq[char] += 1
    # Min_val needed to determine when the first of any key gets exhausted such that we cannot
    # build our full balloon
    min_val = float("inf")
    for char in freq:
        # Grab count of current dictionary character
        char_freq = freq[char]
        # Since O and L occur twice it has a dependency count of 2 in order to be built
        if char == "O" or char == "L":
            # To account for 2X dependency divide by 2
            char_freq /= 2

        min_val = min(min_val, char_freq)

    return int(min_val)
