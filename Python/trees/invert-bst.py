# Function to take a BST and invert it
# Idea: preform BFS, for every element that gets popped from queue,
# swap the left and right children of that element until the queue is empty
# TC: O(n) time | O(n) space
def invertBinaryTree(tree):
    # set queue to root node of our BST
    queue = [tree]
    # While queue is not empty do thos
    while len(queue):
        # obtain node from popping index 0 of queue
        current = queue.pop(0)
        if current is None:
            # case where we append a None value into queue which means we hit a leaf
            continue
        swapLeftAndRight(current)
        # Now append the current nodes that are in final position to the queue
        queue.append(current.left)
        queue.append(current.right)

# swap left and right values of the root tree, swap left child with right child
def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left
