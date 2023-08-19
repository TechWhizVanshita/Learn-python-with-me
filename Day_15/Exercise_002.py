# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

#https://docs.python.org/3/library/time.html#time.strftime

# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.

import time

timestamp = int(time.strftime('%H'))

if(timestamp>=17 and timestamp<=19):
    print("Good Afternoon!")
    
elif(timestamp>=20):
    print("Good Night!")
    
else:
    print("Good Morning!")
