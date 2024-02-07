def number(str):
    count=0
    for i in range(0,len(str)):
        if(str[i]!=" "):
            count=count+1
    return count
str=input("Enter string:")

print("Total no: of character is:",number(str))