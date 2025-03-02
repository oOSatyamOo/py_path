# To create a python generator, we use the yield statement, inside a function, instead of the return
# statement. Let’s take a quick example.

# A generator in Python is a special type of iterator that allows you to generate values
# on the fly without storing the entire sequence in memory. Generators are created using functions with the yield keyword and are especially useful for handling large datasets or streams of data efficiently.

## 2 second time and 3 third time
# def simpleGeneratorFun():
#     yield 1            
#     yield 2            
#     yield 3            
   
# # Driver code to check above generat
# print(simpleGeneratorFun())
# for v in simpleGeneratorFun():
#     print(v)



    ##########

# A simple generator for Fibonacci Numbers
def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit: #0<5
        yield a #0
        a, b = b, a + b #a(1)b(1) = 1|,0+1 #a(1),b(1) = 1|, 1 + 1 #a(1),b(2) = 2|, 1+2 #a(2) b(5) = 3|,3+2 

  
# Create a generator object
x = fib(9)
  
# Iterating over the generator object using next
# print(x.next()) # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
# Iterate through the generator
print(next(x))  # Output: 1
print(next(x))  # Output: 2
print(next(x))  # Output: 3
# print(next(gen))  # Raises StopIteration

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
# for i in fib(5):
#     print(i)

# def even_squares(x):
#   for i in range(x):
#     if i**2%2==0:
#       yield i**2
      
# print(list(even_squares(10)))
# Generator Expression
# Generator expressions are a concise way to create generators, similar to list comprehensions but using parentheses () instead of square brackets [].
# Example: Generator Expression
# # Generator to create squares of numbers
# gen_exp = (x**2 for x in range(5))
# # Iterate through the generator
# for value in gen_exp:
#     print(value)
    
# Python List vs Generator in Python
# This is a very simple difference. A list holds a number of values at once. But a Python generator holds only one value at a time, the value to yield.
# Python Generator vs Function
# when a function stops executing, its local variables are destroyed. This is not the same with a Python generator. Take a look
# list comprehension
# We can use expressions to create python generators shorthand. Let’s take a list for this.
# >>> mylist=[1,3,6,10]
# >>> (x**2 for x in mylist)
# a=(x**2 for x in mylist)
# >>> next(a)
# Output
# 1
# >>> next(a)
# Output
# 9
# >>> next(a)
# Output
# 36
# >>> next(a)
# Output
# 100
# >>> next(a)



# Key Characteristics of Generators
# Laziness:
# Generators produce values one at a time, only when requested, rather than computing and storing all values at once.
# This makes them memory-efficient, especially for large sequences.
# Stateful:
# Generators maintain their state between successive calls, meaning they "remember" where they left off.
# One-Time Use:
# Generators can be iterated over only once. After the generator is exhausted, you must recreate it to iterate again.
# Created with yield:
# Unlike a regular function that uses return to produce a single value and exit, a generator function uses yield to produce a value and pause execution.

# Each time the generator’s __next__() method (or the next() function) is called:
# The generator resumes execution from where it paused.
# It runs until the next yield statement.
# The value after yield is returned.

# Use Cases of Generators
# 1. Infinite Sequences
# Generators can produce infinite sequences since they don’t store the entire sequence in memory.
# Example:
# def infinite_numbers(start=0):
#     while True:
#         yield start
#         start += 1
# # Generate an infinite sequence
# gen = infinite_numbers()
# print(next(gen))  # Output: 0
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2

# 2. Streaming Data
# For processing large streams of data (e.g., logs, files, or network requests) without loading them entirely into memory.
# Example: Read File Line by Line
# def read_large_file(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line
# for line in read_large_file("large_file.txt"):
#     print(line.strip())

# 3. Pipelining
# Generators are great for pipelining operations, such as processing data in stages.
# Example:
# def generate_numbers():
#     for i in range(10):
#         yield i

# def filter_even_numbers(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             yield num

# def square_numbers(numbers):
#     for num in numbers:
#         yield num**2

# # Combine generators in a pipeline
# numbers = generate_numbers()
# even_numbers = filter_even_numbers(numbers)
# squared_numbers = square_numbers(even_numbers)

# print(list(squared_numbers))  # Output: [0, 4, 16, 36, 64]