#https://holypython.com/beginner-python-exercises/exercise-16-defining-functions/

################################################
#Exercise 16-a
#Define a function named f_1 which will print "Hello World!"

print('Exercise 16-a')
def f_1():
    print("Hello World!")
f_1()

################################################
#Exercise 16-b
#Now define the same function f_1 and assign it to variable ans_1. See what happens.

print('Exercise 16-b')
def f_1():
    return "Hello World!"

ans_1= f_1()
print(ans_1)

################################################

#Exercise 16-c
#Now define the same f_1 function this time so that
# it returns a value instead of just printing it..
def f_1():
    return "Hello World!"

ans_1=f_1()
print(ans_1)
################################################

#Exercise 16-d
#Now create a function named f_1 which both prints and returns "Hello World!"

print('Exercise 16-d')
def f_1():
    print('Hello World!')
    return 'Hello World!'

ans_1=f_1()
print(ans_1)
################################################

#Exercise 16-e
#Create a function named f_1 which always returns the number: 100 .

print('Exercise 16-e')
def f_1(val):
    return 100

print(f_1(999))
################################################

#Exercise 16-f
#Create a function named f_1 which takes an integer as input and then returns it.

print('Exercise 16-f')
def f_1(x):
    return x

print(f_1(44))
################################################

#Exercise 16-g
#Can you define a function that takes a list as input and returns the reverse of that list?

print('Exercise 16-g')
lst=[100,200,300,400,500]

def f_1(list):
    return lst.reverse()

f_1(lst)
print(lst)
################################################

#Exercise 16-h
#Write a function named f_1 which will ask user for their name and print Hello!, Name

print('Exercise 16-h')
def f_1():
    name = input("What's your name?")
    print("Hello!, "+ name)

f_1()
################################################
