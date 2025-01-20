# Key Features
# Decorators allow you to extend or modify behavior without changing the original function or class.
# They are implemented using the @decorator_name syntax (syntactic sugar).
# Decorators are often used in Python frameworks (e.g., Flask, Django) for routing, middleware, and more.

# - A decorator is a function that takes another function or class as input and returns a new function or class with additional functionality.
# - Decorators are often used to wrap functions or methods with custom behavior, like logging, access control, or measuring execution time

# Built-in Decorators
# Python has several built-in decorators for common tasks:
# @staticmethod: Defines a static method in a class.
# @classmethod: Defines a class method in a class.
# @property: Makes a method behave like an attribute.
# @functools.lru_cache: Caches function results to speed up repeated calls.

# Real-World Applications
# Web Frameworks:
# Frameworks like Flask and Django extensively use decorators for authentication (@login_required, @permission_required).
# APIs:
# Protect sensitive endpoints in REST or GraphQL APIs by checking for valid tokens (e.g., JWT or OAuth) using decorators.
# Command-Line Tools:
# Add authentication for CLI commands to restrict access to certain operations based on user credentials.

# How Decorators Work
# Takes a function as an argument.
# Defines a wrapper function that adds extra behavior.
# Returns the wrapper function, which replaces the original function
# def decor(func):
#   def wrap():
#     print("$$$$$$$$$$$$$$$$$$$$$$")
#     func()
#     print("$$$$$$$$$$$$$$$$$$$$$$")
#   return wrap
# def sayhello():
#           print("Hello")
# newfunc=decor(sayhello)
# newfunc()


# def divide(a,b):
#     return a/b
# def decorator(func):
#     def wrapper(a,b):
#            if b==0:
#                print("Can't divide by 0!")
#                return
#            return func(a,b)
#     return wrapper


# def divide(a,b):
#     return a/b
# def decorate(func):
#     def wrapper(*args,**kwargs):
#        if args[1]==0:
#            print("Can't divide by 0!")
#            return
#        return func(*args,**kwargs)
#     return wrapper
# divide=decorate(divide)
# divide(2,0)

# # ######################
# Example: A Simple Decorator
# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper
# # Using the decorator
# @my_decorator
# def say_hello():
#     print("Hello!")
# # Call the decorated function
# say_hello()

# Use Cases for Decorators #########################

#1. Logging
# Add logging functionality to a function:
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned: {result}")
#         return result
#     return wrapper
# @log_decorator
# def add(a, b):
#     return a + b
# add(2, 3)

# 2.Timing
# Measure the execution time of a function:
# import time
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
#         return result
#     return wrapper
# @timing_decorator
# def slow_function():
#     time.sleep(2)
#     print("Finished slow function")
# slow_function()

# OutPUT
# Finished slow function
# slow_function took 2.0001 seconds


# 3. Access Control
# def requires_permission(user_role):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if user_role != "admin":
#                 print("Access denied")
#                 return
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
# @requires_permission("admin")
# def view_dashboard():
#     print("Welcome to the dashboard!")
# view_dashboard()


# 4. Repeating a Function
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
# @repeat(3)
# def greet():
#     print("Hello!")
# greet()

# Authentication with a Decorator #############

# def requires_authentication(func):
#     def wrapper(user, *args, **kwargs):
#         if not user.get("is_authenticated"):
#             print("Access Denied: User not authenticated")
#             return
#         print(f"User {user['username']} is authenticated.")
#         return func(user, *args, **kwargs)
#     return wrapper

# @requires_authentication
# def view_dashboard(user):
#     print("Welcome to the dashboard!")

# # Example usage
# user1 = {"username": "Alice", "is_authenticated": True}
# user2 = {"username": "Bob", "is_authenticated": False}

# view_dashboard(user1)  # Authenticated user
# view_dashboard(user2)  # Not authenticated

# Use Case: Role-Based Access Control
# You can also use decorators for role-based authentication, where access is granted based on the user’s role (e.g., admin, editor, viewer).

# Role-Based Example

# def requires_role(required_role):
#     def decorator(func):
#         def wrapper(user, *args, **kwargs):
#             if user.get("role") != required_role:
#                 print(f"Access Denied: User role '{user['role']}' is not sufficient.")
#                 return
#             print(f"Access Granted: User role '{user['role']}' matches '{required_role}'.")
#             return func(user, *args, **kwargs)
#         return wrapper
#     return decorator

# @requires_role("admin")
# def delete_user(user):
#     print("User has been deleted.")
# # Example usage
# admin_user = {"username": "Alice", "role": "admin"}
# viewer_user = {"username": "Bob", "role": "viewer"}
# delete_user(admin_user)  # Allowed
# delete_user(viewer_user)  # Denied