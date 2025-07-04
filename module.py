eg=input("enter the input:")
lower=[]
upper=[]
digit=[]
prime=[]
eve=[]
odd=[]
symbols=[]
for char in eg:
    if char.isalpha():
        if char.islower():
            lower.append(char)
        if char.isupper():
            upper.append(char)
    if char.isdigit():
        if int(char)%2==0:
            eve.append(char)
        if int(char)%2!=0:
            odd.append(char)
        if int(char) in [2, 3, 5, 7]:
            prime.append(char)
        
    if not char.isalnum() and not char.isspace():
        symbols.append(char)
print(lower,"Lower case")
print(upper,"Upper case")
print(eve,"Even numbers")
print(odd,"Odd numbers")
print(prime,"Prime numbers")
print(symbols,"Special")
