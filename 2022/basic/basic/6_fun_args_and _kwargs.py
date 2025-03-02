
# # Default Argument in Python
# # def myFun(x, y=50):
# # myFun(10)

# # Keyword Argument in Python
# # def student(lastname, firstname):
# # student(firstname='Geeks', lastname='Practice')

# # Positional Arguments
# # student('World','Hello')


#  pass is the null statement in python. Nothing happens when this is 
# encountered. This is used to prevent indentation errors and used as a placeholder.
# What keyword is used to define an empty function or class in Python?
# n = 10
# for i in range(n):

#     # pass can be used as placeholder
#     # when code is to added later
#     pass

# # Arbitrary Keyword  Arguments 
# # *args for variable number of arguments
# def myFun(*argv):
#     for arg in argv:
#         print (arg)
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# # Above In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:
# # *args in Python (Non-Keyword Arguments)
# # **kwargs in Python (Keyword Arguments)
# # *kwargs for variable number of keyword arguments


# # def evenOdd(x):
# #     """Function to check if the number is even or odd"""
    
# #     if (x % 2 == 0):
# #         print("even")
# #     else:
# #         print("odd")


# # # Driver code to call the function
# # print(evenOdd.__doc__)

# def myFun1(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))


# # Driver code
# myFun1(first='Geeks', mid='for', last='Geeks')

# # function with params
# def add(num1: int, num2: int) -> int:
#     """Add two numbers"""
#     num3 = num1 + num2

#     return num3

# # Driver code
# num1, num2 = 5, 15
# ans = add(num1, num2)
# print(f"The addition of {num1} and {num2} results {ans}.")

# # Python program to illustrate
# # *args with first extra argument
# def myFun(arg1, *argv):
#     print ("First argument :", arg1)
#     for arg in argv:
#         print("Next argument through *argv :", arg)
 
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# #########################

# # Python program to illustrate 
# # *kwargs for variable number of keyword arguments
 
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print ("%s == %s" %(key, value))
 
# # Driver code
# myFun(first ='Geeks', mid ='for', last='Geeks') 



# # Python program to illustrate  **kwargs for
# # variable number of keyword arguments with
# # one extra argument.
 
# def myFun(arg1, **kwargs):
#     for key, value in kwargs.items():
#         print ("%s == %s" %(key, value))
 
# # Driver code
# myFun("Hi", first ='Geeks', mid ='for', last='Geeks')  


# #################################

# def myFun(*args,**kwargs):
# 	print("args: ", args)
# 	print("kwargs: ", kwargs)


# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")


# def cube(x): return x*x*x

# # using lambda / anonymous function
# cube_v2 = lambda x : x*x*x

# Lambdas are especially useful when passing small functions as arguments to other functions like map, filter, and reduce.
# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x**2, numbers))

# Sorting a list of tuples by the second element
# data = [(2, 'c'), (1, 'a'), (3, 'b')]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)
# When Not to Use Lambdas
# While lambdas are convenient, they aren't suitable for every case:

# Complex Logic: If the function has multiple statements or complex logic, a named function with def is more appropriate for readability and debugging.
# Reusability: If the function will be used in multiple places, defining it with def and giving it a descriptive name is better.


# def factorial(n):
#     return 1 if (n==1 or n==0) else n*factorial(n-1)


# Here x is a new reference to same list lst
# def myFun(x):
#     # every variable name is a reference
#     x[0] = 20


# # Pass by Reference and Pass by Value
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

# del is used to delete a reference to an object. Any variable or list value can be deleted using del.
# s = "GeeksForGeeks"
# print(s)
# del s
# print(s)

# #Deleting py function
# # del func7
# def myFun(x):
# # When we pass a reference and change the received reference to something else
#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = [20, 30, 40]


# # Driver Code (Note that lst is not modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)



# def swap(x, y):
#     temp = x
#     x = y
#     y = temp

# # Driver code
# x = 2
# y = 3
# swap(x, y)
# print(x)
# print(y)



# # Function to calculate the area of a rectangle
# def calculate_rectangle_area(length, width):
# 	# Assertion to check that the length and width are positive
# 	assert length > 0 and width > 0, "Length and width"+ \
# 				"must be positive"
# 	# Calculation of the area
# 	area = length * width
# 	# Return statement
# 	return area


# # Calling the function with positive inputs
# area1 = calculate_rectangle_area(5, 6)
# print("Area of rectangle with length 5 and width 6 is", area1)

# # Calling the function with negative inputs
# area2 = calculate_rectangle_area(-5, 6)
# print("Area of rectangle with length -5 and width 6 is", area2)



# async: Used to declare a function as asynchronous, allowing it to run concurrently with other tasks.

# import asyncio
# # Define an asynchronous main function
# async def main():
#     await func()
# # Define another async function that prints a message
# async def func():
#     print("Hello, async world!")  
# # Run the main function using asyncio.run
# asyncio.run(main())


# import asyncio
# def func(x, y):
#     return x + y
# @asyncio.coroutine
# def do_func(x, y):
#     yield from asyncio.sleep(1)
#     return func(x, y)
# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(do_func(2,3))
# print("Got:", result)
