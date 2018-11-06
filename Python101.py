'''
Created on Nov 5, 2018

@author: skanda
'''
#for i in range(1,11): #Excludes the last number in range
#    print(i)

# Equivalent in while loop
#i = 1
#while i < 11:
#    print(i)
#    i += 1

# Compare two numbers with if elif else
''' Use triple quote or double quote to comment sections
a = 20
b = 20
if a < b:
    print("{} is less than {}".format(a,b))
elif a > b:
    print("{} is greater than {}".format(a,b))
else:
    print("{} is equal to {}".format(a,b))  
'''

'''
import os, glob

#os.chdir("/Users/skanda/Library/Mobile Documents/com~apple~CloudDocs")
os.chdir("/Users/skanda/python-workspace/test")
i = 1
for file in glob.glob("*.py"):
    print(file)
    if i == 10:
        break
    i += 1
'''

'''
# Fizz Buzz print Fizz if divisible by 3, Buzz if divisible by 5 and FizzBuzz if divisible by both
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

'''
# Fibonacci Sequence
a = 0
b = 1
for i in range(0,11):
    print(a)
    x = a
    a = b
    b += x

# Alternative Fibonacci
a,b = 0,1
for i in range(0,11):
    print(a)
    a,b = b, a+b #Note that b gets assigned original a + b


# Fibonacci Generator
# A generator is a function that returns an object (iterator) 
# which we can iterate over (one value at a time).
def fib(num):
    a,b = 0,1
    for i in range(0,num):
        yield "{}: {}".format(i+1,a)
        a,b = b, a+b

for item in fib(10):
    print(item)

'''

'''
# Lists - mutable
mylist = [10,20,30,40,50,60] # Note the square brackets
for i in mylist:
    print(i)

# Tuples - immutable
mytup = (1,2,3,4,5,6,7,8,9,10) # Note the paranthesis
for i in mytup:
    print(i)
'''

'''
#Dictionary - Key / Value pairs in braces {}
mydict = {'FirstName':'Skanda','LastName':'Swamy','Occupation':'Programmer'}
for key,val in mydict.items():
    print("{} is {}".format(key,val))
 
'''    

'''
# Set
myset = {10,10,20,30,40,50,10,60,90}
for i in myset:
    print(i)
'''    

'''
# Print List of squares
mylist = [1,2,3,4,5,6,7,8,9,10]
squares = [i*i for i in mylist]
print(squares) #Don't forget the parantheses around object for print!
'''
 
'''   
# Take input values
name = input("Enter your name: ")
print("Hello " + name + "!") 
'''

int1 = input("Num1: ")
int2 = input("Num2: ")
result = float(int1) + float(int2) # without casting, this will print string concatenation!
print(result)

