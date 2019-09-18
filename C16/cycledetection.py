def succ(a):
    return 0 #returns link from a -> x

##floyd's algorithm
x=0 #starting pointer
a=succ(x)
b=succ(a)
while a!=b: #when meet -- found cycle
    a=succ(a)
    b=succ(succ(b))

a=x
while a!=b:
    a=succ(a)
    b=succ(b)
first=a #first node in cycle

length=1 #length of cycle
b=succ(a)
while a!=b:
    b=succ(a)
    length+=1