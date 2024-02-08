# cook your dish here
t=int(input())
for i in range(t):
    S=input()
    S1="CODETOWN"
    A="AEIOU"
    i=0
    c=0
    while i<len(S):
        if S[i]!=S1[i]:
            if ( S[i] in A) and (S1[i] in A):
                c=c+1
            elif (( S[i] in A) and (S1[i] not in A)) or (( S[i] not in A) and (S1[i] in A)) :
                c=c+0
            elif ( S[i] not in A) and (S1[i] not in A):
                c=c+1
            else:
                c=c+0
        else:
            c=c+1
        i=i+1
    if c==8:
        print("yes")
    else:
        print("no")
