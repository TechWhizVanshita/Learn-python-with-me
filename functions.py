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


#Keyword arguments(kwargs)

def my_function5(girl1,girl2,girl3):
    print("The youngest girl child is " + girl3)
    
my_function5(girl1="Aasma",girl2="Rehnuma",girl3="Sidra")


#Arbitrary keyword arguments(**kwargs)

def my_function6(**boys):
    print("His first name is " + boys["fname"])

my_function6(fname = "Ashu", lname = "Soni")


#Default parameter value -- If we call the function without argument, then it uses default value.

def my_function7(city = "Jhansi"):
    print("I am from " + city)
    
my_function7("Hyderabad")
my_function7("Bengaluru")
my_function7()
my_function7("Delhi")
my_function7("Mumbai")


#passing a list as an argument --

def my_function8(food):
    for x in food:
        print(x)
        
food = ["Pavbhaji","Puchka","Ice-cream"]
my_function8(food)


#Return values

def my_function9(x):
    return x/2

print(my_function9(2))
print(my_function9(10))
print(my_function9(20))


#The pass statement:

def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement
