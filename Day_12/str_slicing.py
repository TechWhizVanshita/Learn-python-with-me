fruit = "pineapple"
fr_len = len(fruit)
print("The length of",fruit,"word is ",fr_len)

print(fruit[0:4]) # 4 not included

print(fruit[:4]) #Slicing from the start but 4 not included

print(fruit[4:]) #Slicing starts from index 4 to the end

# Negative indexing(It always starts from the end.)

print(fruit[-7:-3]) # -7 not included

print(fruit[0:-5]) #Here 0 starts from the starting and output is : pine

print(fruit[-1:len(fruit) - 3]) # It will not throw any output or error.

#Loop through a string:

alphabets = "ABCDE"
for i in alphabets:
    print(i)