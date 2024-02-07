def merge(d1,d2):
    result=d1|d2
    return result
d1={"a":"2","b":"3"}
d2={"c":"4","d":"5"}
d3=merge(d1,d2)
print("The merged dic :",d3)