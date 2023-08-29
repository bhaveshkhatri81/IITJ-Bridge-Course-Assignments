def evaluate_postfix_expression(expression):
    def apply_operator(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b

    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression.")
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(token, a, b)
            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression.")

    return stack[0]


if __name__ == "__main__":
    expression = "1 3 3 * + 9 -"
    result = evaluate_postfix_expression(expression)
    print("Output:", result)
