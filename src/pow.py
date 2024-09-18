def pow(a,n):
    if n == 0:
        return 1
    if n % 2 ==0:
        r = pow(a,n/2)
        return r * r
    r = pow(a,(n-1) / 2)
    return a * r * r

pow(5,100)
