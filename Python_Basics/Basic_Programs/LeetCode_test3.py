def reverse(x):
    rev_no = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)  # Convert x to its absolute value to handle negative numbers
    while x != 0:
        idigit = x % 10
        x = x // 10
        rev_no = (rev_no * 10) + idigit

    return rev_no * sign

print(reverse(-123))

