# b=8
# def func():
#             a=7
#             print(a)
#             print(b)              
# func()

# //global scop prob
# a=1
# def counter():
#                 a=2
#                 print(a)            
# counter()
# solution
a=1
def counter():
                global a
                a=2
                print(a)    
counter()

# Nonlocal keyword
# a = 15
# b = 10

# def add():
  
#       # Add global variables a and b
#     c = a + b  
#     print(c)

# add()  # Output: 25

# def fun():
  
#   # Local variable in fun()
#     var = 10  

#     def gun():
      
#           # Modify var1 in the enclosing scope (fun)
#         nonlocal var  
#         var += 10  
#         print(var)  

#     gun() 

# fun() # Output: 20



# Here i is getting declaired outside for loop not inside
for i in 'selfhelp':
    pass

print(i)# so print can access that

# Initializing variables
a = "hello"
b = 42
 
# Asserting the type of a variable
assert type(a) == str
assert type(b) == int


# Python 3 code to demonstrate 
# working of assert 
# Application

# initializing list of foods temperatures
batch = [ 40, 26, 39, 30, 25, 21]

# initializing cut temperature
cut = 26

# using assert to check for temperature greater than cut
for i in batch:
	assert i >= 26, "Batch is Rejected"
	print (str(i) + " is O.K" )

