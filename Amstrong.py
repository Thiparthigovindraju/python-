n=153
num=n
s=0
while n>0:
    x=n%10
    s+=x**3
    n//=10
if s==num:
    print(num,"is a Amstrong number")
else:
     print(num,"is Not a Amstrong number")
    
