num=5893
s=0
m=1
while num!=0:
    n=num%10
    s+=n
    m*=n
    print(n)
    num//=10
print(s)
print(m)
