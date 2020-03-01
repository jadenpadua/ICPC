Learn more or give us feedback
# O(n) time | O(1) space
def kadanesAlgorithm(array):
	maxEndingHere = array[0]
	maxSoFar = array[0]
	for num in array[1:]:
		maxEndingHere = max(maxEndingHere + num, num)
		maxSoFar = max(maxSoFar, maxEndingHere)
	return maxSoFar
		
