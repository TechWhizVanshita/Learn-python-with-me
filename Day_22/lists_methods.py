#append() - to add an item to the end of the list

list_1 = ["one","two","three","four"]
list_1.append("five")
print(list_1)


#extend() - to append elements from another list

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#in extend() method you can append any type of iterable object.

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)