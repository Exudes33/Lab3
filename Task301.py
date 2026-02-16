def is_valid(n):
    c = str(n)
    for digit in c:
        if int(digit) % 2 != 0:
            return False
    return True



input_n = input()

    if is_valid(input_n):
        print("Valid")
    else:
        print("Not valid")

