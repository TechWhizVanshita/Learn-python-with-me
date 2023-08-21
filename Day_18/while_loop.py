#While loop

i = 2
while i<=20:
    print(i)
    i +=2
    
#The break statement
i = 1

while i<=10:
    print(i)
    if i ==7:
        break
    i += 1
    

#The continue statement

i = 0
while i<10:
    i += 1
    if i==5:
        continue
    print(i)
    
#The else statement

i = 3

while i<=18:
    print(i)
    i += 3
else:
    print("Loop ends!")