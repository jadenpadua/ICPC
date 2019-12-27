# Calculate min number of edit operations to turn one string into another string
# 3 operations: Insert, substitution, deletion

# Idea: Dynamic programming is our friend here, solve problem in small parts,
# and combine those small parts with other small parts to build final solution
# We make a 2d array, let str 1 be the column and str 2  be row
#    " " y a b d
# " "  
#  a
#  b
#  c
#
# now compare min number of operations at each point
# TC O(nm) where n and m are len of str1 and str1 | O(nm) space
def levenshteinDistance(str1, str2):
    # init our 2d edits array that maps the characters in both str1 and str2
    # Populate values like so [0, 1, 2, 3, 4....] in first row, this is base case
    #                         1
    #                         2 
    edits = [[x for x in range(len(str1)+ 1)]for y in range(len(str2)+ 1)]
    # Now gives us our first column that goes from 0 to whatever len our string is
    for i in range(1, len(str2)+ 1):
        edits[i][0] = edits[i - 1][0] + 1
    #Now double for loop iterating through all values inside of our pre defined base cases
    for i in range(1, len(str2)+ 1):
        for j in range(1, len(str1) +1):
            # Checking if the strings are the same, we do -1 to account for the ""
            if str2[i-1] == str1[j-1]:
                # if two string comparisons in fact are equal then just explore diagonal for answer
                edits[i][j] == [i -1][j-1]
            else:
                # Else apply levenshtein distance, add one operatin and take min of three neighbors
                edits[i][j] = 1 + min(edits[i-1], edits[i][j-1], edits[i-1][j])        
    # Return final final value in our 2d array which is the min operations of those two entire strings
    return[-1][-1]

    
