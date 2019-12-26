# Given a string and a key int, shift each letter in that string by the amount of
# spaces defined in the key
def letterShifter(string, key):
    # Create new letters array for our letters we will shift later
    newLetters = []
    # Wrap around function in the event of a key that it is above 26, wrap it around the range
    newKey = key % 26
    # iterate through every ketter in our string
    for i in range(len(string)):
        # now we append that new letter after we shift it to new letter array
        newLetters.append(shiftLetter(string[i], newKey))
    # Join new letters array at the very end
    return ''.join(newLetters)

def getNewLetter(letter, key):
    # Now obtain new letter code and shift with key
    newLetterCode = ord(letter) + key
    # Need to account for wrapping around back to z, since, 122 is z and 97 is a,
    # Lets say we pass in 124, 124 % 122 = 2, our letter is 122(z) and shift is 2
    # so return b, so 96 + 124 % 122 = 98 which is b
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)
