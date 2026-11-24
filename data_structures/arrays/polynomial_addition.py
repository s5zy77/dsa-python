def add_polynomials(poly1, poly2):
    # Each polynomial is represented as a list of coefficients where index = power
    n1 = len(poly1)
    n2 = len(poly2)
    max_len = n1 if n1 > n2 else n2
    result = [0] * max_len

    for i in range(n1):
        result[i] += poly1[i]
    for i in range(n2):
        result[i] += poly2[i]

    return result


def display_poly(poly):
    terms = []
    for power in range(len(poly) - 1, -1, -1):
        coeff = poly[power]
        if coeff != 0:
            if power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
    return " + ".join(terms) if terms else "0"


if __name__ == "__main__":
    # 5 + 0x + 10x^2 + 6x^3
    p1 = [5, 0, 10, 6]
    # 1 + 2x + 4x^2
    p2 = [1, 2, 4]
    total = add_polynomials(p1, p2)
    print("P1:", display_poly(p1))
    print("P2:", display_poly(p2))
    print("Sum:", display_poly(total))