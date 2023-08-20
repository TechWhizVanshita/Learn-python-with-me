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
   
   
for b in range(1,31,1):
    print(b) 
    
#Else in for loop

for x in range(2,8):
    print(x)   
else:
    print("Finished!")
    
#else block not be executed if there is a break statement

for c in range(4):
    if c == 3:
        break
    print(c)
else:
    print("Finished!")
    
#Nested loops

adj = ["red","big","tasty"]
fruits = ["apple","cherry","guava"]

for x in adj:
    for y in fruits:
        print(x ,y)
        
#The pass statement

#for loop can't be empty, and if we hv no content then we use pass statement to avoid any error.

for i in range(0,2):
    pass