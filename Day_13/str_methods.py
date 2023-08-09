#Strings are immutable. It means they work on your existing string and make it a new string.
a = "Vanshita"

#upper() - Converts a string to upper case.
print(a.upper())

#lower() - Converts a string to lower case. 
print(a.lower())

#strip() - Removes any white spaces before and after the string.
b = "   Hello, Vanshita   "
print(b.strip())

#rstrip() - Removes any trailing characters.
c = "I am fine!!!!!!!!!!"
print(c.rstrip("!"))

#replace() - replaces all occurences of a string with another string.
d = "Stranger things"
print(d.replace("Stranger","Good"))

#split() - splits the given string at the specified instance and returns the seperated strings as list items. 

print(d.split(" "))

#captialize() - turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

e = "bigg boss"
print(e.capitalize())

f = "Bigg boss 16"
print(f.capitalize())


#center() - aligns the string to the center as per the parameters given by the user.

g = "Welcome to my home!"
print(g.center(50))

#We can also provide padding character. It will fill the rest of the fill characters provided by the user.
print(g.center(50,"*"))


#count() - returns the number of times the given value has occured within the given string.

h = "papaya"
print(h.count('a'))

#endswith() - checks if the string ends with a given value. If yes then return True, else return False.

i = "I am a second year student."
print(i.endswith('student.'))

#We can also check for a value in between the string by providing start and end index positions.
j = "Drinking is bad for health."
print(j.endswith("bad",11,15))

#find() - searches for the first occurrence of the given value and returns the index where it is present. If given value is absent then it returns -1.

k = "Getting up early is good for health."
print(k.find("good"))

#find() is similar to index() method but the major difference is that index() raises an exception if value is absent whereas find() returns -1.

print(k.find("bad"))

#index() - searches for the first occurrence of the given value and returns the index where it is present. If given value is absent then it raises an exception.

l = "You are good enough to achieve your dream."
print(l.index("enough"))

# print(i.index("reality"))

#isalnum() - returns true only if entire string consists alphabetic or numeric characters, if any other characters or punctuations are present then it returns False.

#Space is also not allowed in this string method.
m = "Learnpythonwithme"
print(m.isalnum())



#isalpha() - return True only if entire string only consists A-Z, a-z . If any other characters or punctuations or numbers (0-9) are present, then it returns False.

n = "Welocome13"
print(n.isalpha())


#islower() - return True if all the characters in the string are lower case, else it returns false.

o = "My name is Vanshita"
print(o.islower()) #return False

#isprintable() - returns True if all the values within given string are printable. 

# control characters such as (newline,tab,carriage return are not printable character.)

p = "We wish you a Merry Christmas"
print(p.isprintable())

#isspace() - returns True if only and only if the string contain white space or white space characters(newline,tab,carriage return), else returns false.

q = "   "
r = "\t\t\t\t"
s = "Hello, World..."
print(q.isspace())
print(r.isspace())
print(s.isspace())

#istitle() - returns True only if the first letter of each word of the string is captialized, else it returns False.

t = "World Wide Web"
print(t.istitle())

#isupper() - returns True if all the characters present in the string are in the upper case.

u = "MY NAME IS VANSHITA"
print(u.isupper())

#startswith() - checks if the string starts with a given value. If yes then return True, else return False.

v = "Python is Interpreted language."
print(v.startswith("Python"))

#swapcase() - changes the character casing of string. Upper case are converted to lower case and lower case to upper case.

w = "How are you?"
print(w.swapcase())


#title() - captializes each letter of the word within the string.

x = "I live in gargi hostel."
print(x.title())