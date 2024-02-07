def star(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print(" ")
    for i in reversed(range(0,i+1)):
        for j in reversed(range(0,i)):
            print("*",end="")
        print(" ")
    
n=int(input("Enter terms:"))
star(n)