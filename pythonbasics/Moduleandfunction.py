#what is module?
# A module is a file containing Python code. 
# It can define functions, classes, and variables that can be reused in other Python programs.

#Functions in Python
# A function is a block of code that only runs when it is called.>>code reusability

#syntax to define a function
# def function_name(parameters):
#     statements

def add(a,b):
    c = a + b
    return c  #return statement is used to return the value from the function

#calling the function   
print(add(10,20))  #calling the function with arguments 10 and 20
print(add(100,200))  #calling the function with arguments 100 and 200
print(add(1000,2000))

#hands on
#create a function to find the square of a number
#create a function to find the even numbers from n to n