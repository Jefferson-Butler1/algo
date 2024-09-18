import functools
def poly(x, coeffs):
    sum = 0
    for i in range(len(coeffs)):
        sum += coeffs[i] * x**i
    return sum

def poly2(x, coeffs):
    if not coeffs:
        return 0
    return coeffs[0]+x*poly2(x, coeffs[1:])

coeffs = [
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
]
print(poly(2, coeffs))
print(poly2(2, coeffs))
