n=5
#half piramide
for i in range(n+1):
    print("*"*i)
for i in range(n+1,0,-1):
    print("*"*i)

#half piramide
re=1#repet
for i in range(n):
    
    spece=n-i
    le_re=re-1
    print(" "*spece, '*'*re,'*'*le_re,sep="")
    re+=1