def gcd (a, b):
    while b != 0:
        anew = b
        b = a % b
        a = anew
    return a
