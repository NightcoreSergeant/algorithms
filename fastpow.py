def pow(a,x):
    if x==0:
        return 1
    if x%2==1:
        return (pow(a,x//2)**2)*a
    elif x%2==0:
        return pow(a,x//2)**2

def slow(a,x):
    s=1
    for _ in range(x):
        s*=a
    return s
