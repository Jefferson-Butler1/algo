a = [[2, 3], [5, 1]]
b = [[8, 6], [0, 4]]

def dotProd(a,b):
    return sum([x*y for x,y in zip(a,b)])

def matMult(a, b):
    n = len(a)
    result = [[0 for _ in a[0]] for _ in a]
    for i in range(len(a)):
        for ii in range(len(b[0])):
            for x in range(len(a[0])):
                result[i][ii] += a[i][x] * b[x][ii]
    return result

print(matMult(a,b))

