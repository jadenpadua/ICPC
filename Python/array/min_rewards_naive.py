def minRewards(scores):
	#init rewards array
	rewards = [1 for _ in scores]
	# start at first index 
	for i in range(1, len(scores)):
			# make two pointers, i and trailing pointer j
			j = i - 1
			# if pointer i is bigger just increment and keep goin
			if scores [i] > scores[j]:
				rewards[i] = rewards[j] + 1
			# if pointer j is bigger we need to fix all previous indexes of rewards
			else:
				# while in boounds and scores of j is smaller than j + 1
				while j >= 0 and scores[j] > scores[j+1]:
					# calculate our new rewards[j] when traversing backwards in array
					# we do max here bc we do not neccessarily have to fix j
					# we don't need to fix rewards j if it is already bigger previously
					rewards[j] = max(rewards[j], rewards[j+1] + 1)
					j -= 1
	return sum(rewards)
