def precedence(op):
    if op in ("+", "-"):
        return 1
    if op in ("*", "/", "%"):
        return 2
    if op == "^":
        return 3
    return 0


def is_right_associative(op):
    return op == "^"


def infix_to_postfix(expr):
    stack = []
    output = []

    for ch in expr:
        if ch == " ":
            continue
        if ("a" <= ch <= "z") or ("A" <= ch <= "Z") or ("0" <= ch <= "9"):
            output.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while len(stack) > 0 and stack[-1] != "(":
                output.append(stack.pop())
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
        else:
            while (
                len(stack) > 0
                and stack[-1] != "("
                and (
                    precedence(stack[-1]) > precedence(ch)
                    or (precedence(stack[-1]) == precedence(ch) and not is_right_associative(ch))
                )
            ):
                output.append(stack.pop())
            stack.append(ch)

    while len(stack) > 0:
        output.append(stack.pop())

    return "".join(output)


if __name__ == "__main__":
    infix = "A+(B*C-(D/E^F)*G)*H"
    print("Infix:  ", infix)
    print("Postfix:", infix_to_postfix(infix))