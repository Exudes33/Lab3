def is_valid(n):
    s = str(n)
    for digit in s:
        if int(digit) % 2 != 0:
            return False
    return True


try:
    input_n = input().strip()
    
    if is_valid(input_n):
        print("Valid")
    else:
        print("Not valid")
except EOFError:
    pass
