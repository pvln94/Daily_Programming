def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            if len(stack) < 2:
                raise ValueError("Insufficient operands in the stack.")
            operand2, operand1 = stack.pop(), stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(int(operand1 / operand2))
            elif token == '^':
                stack.append(int(operand1 ** operand2))
            else:
                raise ValueError(f"Unknown operator: {token}")
    
    if len(stack) != 1:
        raise ValueError()
    
    return stack[0]

expression = input("Enter a postfix expression: ")
try:
    result = evaluate_postfix(expression)
    print(result)
except Exception as e:
    print("ERROR!", str(e))
