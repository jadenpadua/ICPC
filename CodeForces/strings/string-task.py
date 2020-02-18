def main():
	vowels = ["a","e","i","o","u","y"]
	output = ""
	string = input()
	for i in range(len(string)):
		if string[i].lower() in vowels:
			continue
		if string[i].isupper():
			output = output + "." +  string[i].lower()
			continue
		output = output + "." +  string[i]
	print(output)
	
		
main()
