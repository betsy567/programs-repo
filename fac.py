def factorial(n):
    f=1
    if n==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            f=f * i
        print("factorial of",n ,"is",f)
n=int(input("Enter number:"))
factorial(n)