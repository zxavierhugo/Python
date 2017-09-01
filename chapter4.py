"""
4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
"""



def computepay(h,r):
    if (h > 40):
        value = ((h - 40)*1.5+40)*r
    else:
        value = h*r
    return value

try:
    hours = float(input('Enter Hours: \n'))
    rates = float(input('Enter Rate: \n'))
    y = computepay(hours, rates)
    print('Pay:' + str(y))
except:
    print('Error. Please input again')

#---------

"""""
#Practise
def computegrade(grade):
    if (grade >= 0.9 and grade <= 1.0):
        print('A')
    elif (grade >= 0.8 and grade <0.9):
        print('B')
    elif (grade >= 0.7 and grade <0.8):
        print('C')
    elif (grade >= 0.6 and grade <0.7):
        print('D')
    elif (grade >= 0 and grade < 0.6):
        print('F and Bad score')
    else:
        print('Score is out of range. Please input the score within 0 and 1.0.')

try:
    scores = float(input('Enter score'))
    computegrade(scores)

except:
    print('Please input numbers')

#-----

import random
for i in range (10):
    x = random.random()
    print(x*10)

y = random.randint(5,10)
print('\n' + str(y))

t = [1,2,3,6,7,8,20, 26]
print(random.choice(t))

import math
radians = 0.7
print(math.sin(radians))

degrees = 45
print(degrees/360.0*2*math.pi)

print(math.sqrt(2)/2.0)

def print_lyrics():
    print("Will you still love me tomorrow?")
    print("Tonight you are mine completely.")

print_lyrics()

def repeatlyrics():
    print_lyrics()
    print_lyrics()

repeatlyrics()

def print_twice(test):
    print(test)
    print(test)
#print(print_twice('Adrian '*2))
print_twice('Adrian')

print_twice('tomorrow')
result = print_twice('tomorrow')
result
print(result)


def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)

def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()

#print(jane())
#print(fred())
#print(jane())
"""""
