def log(a,b):
    
    if(b > a):
        return 1 + log(a,b/a)
    if(b==a):
        return 1
    return 0

