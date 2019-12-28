# Given a 2d array with 0's and 1's, determine the sizes of all rivers
# (all streaks where there are 1's) and return in output array
# runs in O(wh) time | O(wh) space where w is width and h is height of 2d array
# regarding space complexity, w is width of aux array and h is height of aux array
def riverSizes(matrix):
    # init our output sizes array
    sizes = []
    # init visited aux array to all false boolean values
    visited = [[False for value in row]for row in matrix]
    # Traverse through 2d array
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # case where already visited, do not traverse
            if visited[i][j]:
                continue
            # explore all nodes around it in DFS manner
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    # init size of current river
    currentRiverSize = 0
    # pass in point that we need to explore for our nodes
    nodesToExplore = [[i, j]]
    # While still len of nodes to explore in stack
    while len(nodesToExplore):
        # pop point in nodesToExplore 
        currentNode = nodesToExplore.pop()
        # get coordinates of i and j indexes in our currentNode point
        i = currentNode[0]
        j = currentNode[1]
        # if node we are explolring already marked as visited do not count this
        if visited[i][j]:
            continue
        # Else we need to mark visited to true here
        visited[i][j] = True
        # if it is land then stop exploration here
        if matrix[i][j] == 0:
            continue
        # else we know this node is a possible river so increment cur river size
        currentRiverSize += 1
        # Now get all unvisited neighbors of this valid node and traverse through them
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        # now push these neighbors onto our stack and conduct DFS
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
        # if > 0 then append our current river size to output array
        if currentRiverSize > 0:
            sizes.append(currentRiverSize)
# Method to get all four neighbors of root '1' node (DFS)
def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    # checking if top neighbor is valid
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbors.append([i - 1, j])
      # checking if bottom neighbor is valid
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeighbors.append([i + 1, j])
      # checking if left neighbor is valid
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbors.append([i, j-1])
      # checking if right neighbor is valid
    if j < len(matrix[0]) and not visited[i][j+1]:
        unvisitedNeighbors.append([i, j+1])
    return unvisitedNeighbors
