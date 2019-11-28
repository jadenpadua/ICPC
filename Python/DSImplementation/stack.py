string = "Hello World"

stack = []
for i in range(len(string)):
    stack.append(string[i])

print(stack)

for i in range(len(stack)):
    print(stack.pop())
