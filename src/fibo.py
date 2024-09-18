import sys

def fibo_rec(n):
    if n < 2:
        return n
    return fibo_rec(n-1) + fibo_rec(n-2)

def fibo_iter(n):
    results = [0,1]
    for i in range(2,n+1):
        results.append(results[-2] + results[-1])
    return results[-1]

num = 6
print(sys.argv, len(sys.argv))
if(len(sys.argv) > 1 ):
    num = int(sys.argv[1])

print(fibo_rec(num))
print(fibo_iter(num))
