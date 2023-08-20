#for in list

students = ["anubha","tanisha","vanshita"]
for y in students:
    print(y)
    
#Looping through a string

for x in "Vanshita":
    print(x)
    

#The break statement

fruits = ["Guava","Cherry","Tomato"];
for x in fruits:
    print(x)
    if x == "Cherry":
        break
    
    
pickle = ["mango","carrot","garlic"];
for p in pickle:
    if p == "carrot":
        break
    print(p)
    
    
#The continue statement

name = ["Ram","Anuj","Anup","Gita","Shiv"];
for n in name:
    if n == "Anup":
        continue
    print(n)
    
#The range() function

#print values from 0 to 9
for x in range(0,10):
    print(x)
 
#print values from 1 to 10   
for a in range(1,11):
    print(a)
    