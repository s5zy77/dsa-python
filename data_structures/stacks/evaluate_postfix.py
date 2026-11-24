def evaluate_postfix(expr):
    stack = []
    tokens = expr.split()

    for token in tokens:
        if token.isdigit() or (token[0] == "-" and len(token) > 1 and token[1:].isdigit()):
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
            elif token == "^":
                stack.append(a ** b)

    return stack[0]


if __name__ == "__main__":
    # Space-separated tokens handle multi-digit operands cleanly
    postfix_expr = "10 2 8 * + 3 -"
    print("Postfix Expression:", postfix_expr)
    print("Evaluated Result:  ", evaluate_postfix(postfix_expr))