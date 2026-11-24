def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


if __name__ == "__main__":
    print("GCD(48, 18):", gcd_recursive(48, 18))