l1=[1,2,3,4,5]
l2=[2,6,7,8,9]
if(len(l1)==len(l2)):
    print("same length")
else:
    print("not same")
#same value
a=set(l1)
b=set(l2)
if a==b:
    print("l1 and l2 same values")
else:
    print("both are not equal")
#common
for i in range(len(l1)):
    if i in l2:
        print(i)