# Define a function to return all substrings of a particular string
def allSubstringsOfString(string):
    # init substrings array
    substrings = []
    # two pointer looping throuhg string
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i : j])
    return substrings

print(allSubstringsOfString("Hello"))
