
def gcd(a,b):
    if b==0:
        return a
    else:
        return b
    if a<b:
        small=a
    else:
        small=b
    for i in range(1,small+1):
        if a % i==0 and b % i==0:
            g=i
    return g

a=int(input("Enter a:"))
b=int(input("Enter b:"))
res=gcd(a,b)
print(res)