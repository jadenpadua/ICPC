# Given a string with three bracket types determine if said brackets are balanced
# TC: O(n) because you are iterating through bracket string all in constant time operations
# SC: O(n) because you are storing n elements in the stack at worst csae
def balancedBrackets(string):
    # need to init closing and opening brackets string to see if element to compare is in that string
    openingBrackets = "([{"
    closingBrackets = ")]}"
    # hashtable to map all closing brackets to opening brackets
    matchingBrackets = { "}": "{","(": ")", "}":"{" }
    #init our stack
    stack = []
    for char in string:
        # if char is indeed an opening bracket we must append to stack
        if char in openingBrackets:
            stack.append(char)
        # if char is closing bracket we must consider two cases
        elif char in closingBrackets:
            # if initial value in stack is closing we can automatically assume false
            if len(stack) == 0:
                return False
            # now check if last value of stack matches our value assigned to the closing bracket in hashtable case is valid
            if stack[-1] == matchingBrackets[char]:
                # pop final value from stack
                stack.pop()
            # if not match must return false, invalid here
            else:
                return False
    # final check if our stack is 0 then we know it is clear and valid 
    return len(stack) == 0

