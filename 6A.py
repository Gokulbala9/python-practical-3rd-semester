def get_precedence(operator):
    if operator in ('+', '-'):
        return 1
    if operator in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(infix_expression):
    stack = []
    postfix_output = []
    infix_expression = infix_expression.replace(" ", "")
    
    for char in infix_expression:
        if char.isalnum():
            postfix_output.append(char)
        elif char in ('(', '[', '{'):
            stack.append(char)
        elif char in (')', ']', '}'):
            mapping = {')': '(', ']': '[', '}': '{'}
            target_open = mapping[char]
            while stack and stack[-1] != target_open:
                postfix_output.append(stack.pop())
            if stack:
                stack.pop()
        else:
            while stack and stack[-1] not in ('(', '[', '{') and get_precedence(stack[-1]) >= get_precedence(char):
                postfix_output.append(stack.pop())
            stack.append(char)
            
    while stack:
        postfix_output.append(stack.pop())
        
    return "".join(postfix_output)

if __name__ == "__main__":
    infix_input = input("Enter infix expression: ")
    postfix_result = infix_to_postfix(infix_input)
    print(postfix_result)
