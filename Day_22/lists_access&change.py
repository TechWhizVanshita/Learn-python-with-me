#List is changeable, we can change,add and remove items in it.

thisList = ["Vanshita","Gargi","Falak","Farah"]
print(thisList)


#Allow duplicates

thisList1 = ["Vanshita","Gargi","Falak","Farah","Fiza","Gargi","Falak"]
print(thisList1)

#List - length

print(len(thisList))
print(len(thisList1))

#can contain different data type.

thisList2 = ["abc",21,True,54.1]
print(thisList2)



#type

print(type(thisList))

#The list() constructor:

a = list(("one","two","three"))
print(a)

#Access list items:

print(a[0])
print(a[-1])

#Range of positive Indexes

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5]) #2 (included) and end at index 5 (not included)

print(thislist3[:4]) #Not included index 4

print(thislist3[2:]) #From index 2 to the end


#Range of negative indexes

print(thislist3[-7:-3])

#Check if item exists

if "apple" in thislist3:
    print("Yes",thislist3[0],"is in the fruits list")
    
    
#Change item value

list_1 = ["one","two","three","four"]
list_1[2] = "five"
print(list_1)

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

thislist3[1:3] = ["pineapple","strawberry"]
print(thislist3)

list_2 = ["ink","pen","paper","copy"]
list_2[1:2] = "register","scale" #Here index 2 replace with 2 values.

print(list_2)

list_3 = ["white","green","blue"]
list_3[1:3] = "yellow"

print(list_3)

