# Given three inputs, a top ancestor of an ancestral tree,
# and the two other inputs which are descendents of the ancestral tree,
# Write a function that returns the youngest common ancestor of the
# two descendents
# Note: we can only traverse upwards since we only have access to ancestor property
# need to get two descendents to be on the same level of tree
# so calcuate two descendents depths of the tree
# TC: O(D) where D is the depth ot the lowest descendent
# SC: O(1) constant

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Calculate both depths of descendent nodes
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    # Need if else here to figure out which descendant that is lower
    # if first descendant is lower, then lower desc = descedant One
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    # if second descedant is lower then lower desc = descendant two
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)
# Now starts from descedant node and keeps going up until reaches top ancestor of tree
def getDescendantDepth(descendant, topAncestor):    
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth
# Now backtrack tree give n ower higher descedant and diff between the two descedants
def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    # While there still is a diff in depth between the two descendants
    while diff > 0:
        # go up in tree
        lowerDescendant = lowerDescendant.ancestor
        # decrement our diff
        diff -= 1
    # Now after descedants ar eon level playing field, keep makinf descendants go up
    # until reach same node
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    # Now we know we are at same common ancestor
    return lowerDescendant
