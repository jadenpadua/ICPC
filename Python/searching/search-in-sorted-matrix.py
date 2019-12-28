# Given a sorted 2d matrix, find an element in that matrix
# TC: O(n + m) | SC: O(1), it is n + m because thats how many row and column
# elements you need in order to traverse
def searchInSortedMatrci(matrix, target):
    # Traverse matrix starting at top right corner using while loop
    row = 0
    # last value in first row (top right)
    col = len(matrix[0])  - 1
    # while we have not went through all matrix rows and col, while still valid matrix positions
    while row < len(matrix) and col >= 0:
        # if coordinate is greater, eliminate greater numbers (below it), and go left
        if matrix[row][col] > target:
            # decrementing column will invalidate the last column
            col -= 1
        # if coordinate is smaller, elim smaller numbers so move down the row to elminate nums even smaller
        elif matrix[row][col] < target:
            row += 1
        # if we found our target
        else:
            return [row, col]
    return [-1,-1]
