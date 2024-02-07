def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
n=int(input("Enter no of terms:"))
if n<0:
    print("enter positive number")
else:
    print("The series is:")
    for i in range(n):
        print(fib(i))