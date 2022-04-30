l,b,h=map(int,input().split())
s=(l+b+h)/2
A=(s*(s-l)*(s-b)*(s-h))**0.5;
print(format(A,".2f"))
