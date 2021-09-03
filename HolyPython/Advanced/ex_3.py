#https://holypython.com/advanced-python-exercises/exercise-3-try-except/

#Exercise 3-a:
#Place result="You can't divide with 0" to the right place so that program avoids ZeroDivisionError.

print('Exercise 3-a')

#Type your answer below (pick the correct line).

a=5
b=0
try:
    result=a/b
except ZeroDivisionError:
    result="You can't divide with 0"

print(result)

###########################################################

#Exercise 3-b:
#.get() is not a list method. Place pass keyword to the right line so that program doesn't throw an error.

print('Exercise 3-b')

#Type your code here.
a = [1, 3, 5]
try:
    a.get()
except:
    pass

print(a)

###########################################################

#Exercise 3-c:
#Place msg="You can't add int to string" to the right place so that program avoids BaseExceptionError.
#You can use except Exception although normally you should be careful using such powerful exception statements.

print('Exercise 3-c')

#Type your answer below.

a="Hello World!"
try:
    a + 10
except Exception:
    msg="You can't add int to string" 

print(msg)

###########################################################

#Exercise 3-d:
#Place msg="You're out of list range" to avoid IndexError.

print('Exercise 3-d')
#Type your answer below.
lst=[5, 10, 20]

try:
    print(lst[5])
    
except IndexError:
    msg="You're out of list range"

print(msg)

