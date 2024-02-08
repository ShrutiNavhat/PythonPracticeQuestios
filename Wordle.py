t=int(input())
for i in range(t):
    s=input()
    s1=input()
    i=0
    b=""
    while i<len(s):
        if s[i]==s1[i]:
            b="G"
        else:
            b="B"
        i=i+1
    print(b)
