fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
l=len(fruits)
newlist=[]
for i in range(l-1,-1,-1):
    if len(fruits[i])>5:
        newlist.append(fruits[i])
print(newlist)
