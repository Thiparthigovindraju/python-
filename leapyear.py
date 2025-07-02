year=int(input())
if year%4==0:
    print(year,"is a leap yaer")
elif year%100==0:
    print(year,"is Not a leap yaer")
elif year%400==0:
    print(year,"is a leap yaer")
else:
    print(year,"is Not a leap yaer")
    
