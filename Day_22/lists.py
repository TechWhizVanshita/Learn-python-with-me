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