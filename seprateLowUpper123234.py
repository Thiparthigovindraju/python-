eg=input("enter the input:")
lower=[]
upper=[]
digit=[]
symbols=[]
for char in eg:
    if char.isalpha():
        if char.islower():
            lower.append(char)
        if char.isupper():
            upper.append(char)
    if char.isdigit():
        digit.append(char)
    if not char.isalnum() and not char.isspace():
        symbols.append(char)
print(lower)
print(upper)
print(digit)
print(symbols)
