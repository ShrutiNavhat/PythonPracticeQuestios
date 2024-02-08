t=int(input())
for i in range(t):
    N=int(input())
    S=input()
    i=0
    k=0
    while i<N:
        j=k+1
        while j<N:
            print((S[i]+S[j]))
            j=j+1
        i=i+1
        k=k+1
    
