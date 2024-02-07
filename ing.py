def add(string):
    if string.endswith('ing'):
        string += 'ly'
    elif len(string) >= 3:
        string += 'ing'
    return string
string = input("enter string:")
print(add(string))
