n="govind raju"
vowels="aeiouAEIOU"
newlist=[]
newstr=""
for char in n:
    if char in vowels:
        newlist.append(char)
        newstr+=char
print(newlist)
print(newstr)
