# Function that checks if a string is a palindrome
# O(n) time | O(1) space best approach
# Idea: two pointers, one at start one at end, move pointers until overlap or if strings are same
def isPalindrome(string):
    # Start pointer and end pointer
    leftIdx = 0
    rightIdx = len(string) - 1
    # do until pointers overlap
    while leftIdx < rightIdx:
        # if tow index values are not equal we kno we do not have a problem
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    # Return true if loop breaks
    return True
