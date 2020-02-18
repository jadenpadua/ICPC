def main():
	solutions = 0
	n = int(input())
	for i in range(n):
		arr = list(map(int,input().split()))
		if arr.count(1) >= 2:
			solutions += 1
	return solutions
print(main())
	
