#Create a function

def my_fuction1():
    print("Hello,I am a vanshita.")
    
#Call a function

my_fuction1()

#Arguments -- information can be passed into functions

def my_function2(fname):
    print(fname + " Devi")
    
my_function2("Pushpa")
my_function2("Seema")
my_function2("Pinky")

#Number of arguments -- expects called arguments not less or more than that.

def my_function3(fname, lname):
    print(fname + " " + lname)

my_function3("Vivek","Kumar")

#Arbitrary arguments (*args)

def my_function4(*brothers):
    print("The elder brother is " + brothers[0])

my_function4("Ramesh","Suresh","Sree")