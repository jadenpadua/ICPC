# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

	#O(log(n)) time | O(1) space
    def insert(self, value):
		currentNode = self
		while True:
			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
				currentNode = currentNode.left
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else
				currentNode = currentNode.left
		return self
	
	#O(log(n)) time | O(1) space
    def contains(self, value):
    	currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif:
				currentNode = currentNode.right
			else:
				return True
		return False
	
	# O(log(n)) time and O(1) space
    def remove(self, value, parentNode = None):
		currentNode = self
		while currentNode is not None:
			#Search for it
			if value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value:
				parentNode = cuurentNode
				currentNode = currentNode.right
				#Now when its found
			else:
				# case where currentNode has two children nodes
				if currentNode.left is not None and currentNode.right is not None:
					#value of current Node is smallest value of right subtree
					currentNode.value = currentNode.right.getMinValue()
					#Now remove that smallest right subtree of where we got it from
					currentNode.right.remove(currentNode.value, currentNode)
				
				#case where we are dealing with the root node
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.value
					if currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else:
						currentNode.value = None
					
				#case where we are not dealing with the root node, left child
				elif parentNode.left = currentNode
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				# case where curent Node is a one right child
				elif parentNode.right = currentNode
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break
				
			return self
		def getMinValue(self):
			currentNode = self
			while currentNode.left is not None:
				currentNode = currentNode.left
			return currentNode.value
	
