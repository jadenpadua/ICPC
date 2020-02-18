def main():
	arr1 = list(map(int, input().split()))
	n = arr1[0]
	k = arr1[1]
	arr = list(map(int, input().split()))
	count = 0
	if k > len(arr):
		return ""
	kth_finisher = arr[k-1]
	for i in range(len(arr)):
		if arr[i] > 0 and arr[i] >= kth_finisher:
			count += 1
	return count

print(main())
