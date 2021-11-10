# def my_generator():
#   print("Inside my generator")
#   yield 'a'
#   yield 'b'
#   yield 'c'

# my_generator()

# for char in my_generator():
#   print(char)

# def counter_generator(low, high):
#     while low <= high:
#        yield low
#        low += 1

# for i in counter_generator(5,10):
#   print(i, end=' ')

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

#looping forever
# for i in infinite_sequence():
#   print(i, end=" ")

# 


#returning func from func
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child

# first = parent(1)
# print(first())




#simple decorator

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
    
# @my_decorator #easier way
# def say_whee():
#     print("Whee!")

# # say_whee = my_decorator(say_whee) #if without using @my_decorator

# say_whee()

#---------------------------------------------
#boilerplate for more complex decorators

# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator

#---------------------------------------------

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(start_time)
        print(end_time)
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)