# Given a string, determine the longest substring that is indeed a palindrome in that string
# TC: O(n^2) where n is len of input string, b/c we iterate through array and every point in arr we iterate
# we do two expansions, one at letter and one in between prev letter and current letter, so both expansions operate in O(n) time
# SC: O(1) we are not storing anything, only storing our palindrome result which is constant space
def longestPalinfromicSubstring(string):
    # init our current longest palindrome substring
    # this is just a string sliced index that we can refer to in string later, this is good in order to save space
    # we can init it to our first substr]ing we will encounter in our string
    currentLongest = [0 , 1]
    # now iterate through string, we can start at 1 b/c we know string[0] is already a palindrome
    for i in range(1, len(string)):
        # Now one of our two expansions, this is when our pivot is a letter and we look left and right
        odd = getLongestPalindromeFrom(string, i-1, i+1)
        # Our other expansion, where our pivot is in between current letter and the letter to the left
        even = getLongestPalindromeFrom(string,i-1,i)
        # now grab longest variable which is max between both expansions, use lambda function to determine which substring is greater elegantly
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        # now we can update our current longest accordingly due to the previous iteration
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    # now we can juwst use our current longest and take the substring of those two indeces
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx,rightIdx):
    # if we are still in restrains of string
    while leftIdx >= 0 and rightIdx < len(string):
        # case where left and right index do not match, in this case we shall break out b/c not palindrome
        if string[leftIdx] != string[rightIdx]:
            break
            # else we can expand, valid case
        leftIdx -= 1
        rightIdx += 1
    # now return updated indexes of substring, we need to do leftIdx + 1 to adhere to format of currentLongest array
    return [leftIdx + 1, rightIdx]
