#from list find sum of eve and odd
a=[10,100,20,11,0,5,0,-2,1]
eve=0
odd=0
for i in a:
    if i%2==0:
        eve+=i
    else:
        odd+=i
print(eve)
print(odd)
        
