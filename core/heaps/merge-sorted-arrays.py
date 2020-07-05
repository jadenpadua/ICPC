def mergeSortedArrays(arrays):
	# Output sorted list
	sortedList = []
	# Add all items in first indeces of all n lists
	smallestItems = []
	# Iterating through all arrays, getting smallest items
	for arrayIdx in range(len(arrays)):
		# Store a dict 1st entry tells what array it is on
		# Second entry tells what index the element is on in the array
		# Last entry tells the actual value of that index
		smallestItems.append({"arrayIdx": arrayIdx, "elementIdx": 0, "num": arrays[arrayIdx][0]})
	# Now build our minHeap passing in out smallestItems list
	minHeap = MinHeap(smallestItems)
	# Keep running until minHeap is empty
	while not minHeap.isEmpty():
		# Now remove top value from min heap, it will sift down for you to make sure
		# if you remove something again THAT will be the smallest value
		smallestItem = minHeap.remove()
		# smallest item is a dict, so extract
		arrayIdx, elementIdx, num = smallestItem["arrayIdx"], smallestItem["elementIdx"],smallestItem["num"]
		# now append num value to sorted list
		sortedList.append(num)
		# Check if we are out of bounds in one of our arrays
		if elementIdx == len(arrays[arrayIdx]) - 1:
			# Skip if given array is going to be out of bounds
			continue
		# Now insert next element if given array into our min heap (will sift up for you)
		minHeap.insert({"arrayIdx": arrayIdx, "elementIdx":elementIdx + 1, "num": arrays[arrayIdx][elementIdx + 1]})
	# Now return ultimate sorted list which will get you answer
	return sortedList
		
	
	
class MinHeap:
	def __init__(self, array):
		self.heap = self.buildHeap(array)
	
	def isEmpty(self):
		return len(self.heap) == 0
	
	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
	
	def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != - 1 and heap[childTwoIdx]["num"] < heap[childOneIdx]["num"]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap]["num"] < heap[currentIdx]["num"]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return
	
	def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx]["num"] < heap[parentIdx]["num"]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
	
	def remove(self):
		self.swap(0, len(self.heap)-1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap)-1, self.heap)
		return valueToRemove
	
	def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap)-1, self.heap)
	
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]
