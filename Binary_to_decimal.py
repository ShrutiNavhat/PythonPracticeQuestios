s=input()
i=0
b=0
j=1
while i<len(s):
    if s[-j]=="1":
        b=b+(2**i)
    i=i+1
    j=j+1
print(b)
