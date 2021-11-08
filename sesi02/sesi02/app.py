# print('hello world');

# # 1
# x = 0
# y = 5

# if x < y:                            # Truthy
#     print('yes')

# if y < x:                            # Falsy
#     print('yes')

# if x:                                # Falsy
#     print('yes')

# if y:                                # Truthy
#     print('yes')

# if 'aul' in 'grault':                # Truthy
#     print('yes')

# if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
#     print('yes')

# Does line execute?                        Yes    No
# #                                           ---    --
# if 'foo' in ['foo', 'bar', 'baz']:        #  x
#     print('Outer condition is true')      #  x

#     if 10 > 20:                           #  x
#         print('Inner condition 1')        #        x

#     print('Between inner conditions')     #  x

#     if 10 < 20:                           #  x
#         print('Inner condition 2')        #  x

#     print('End of outer condition')       #  x
# print('After outer condition')            #  x

x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


print('20' if x<50 else "x is large")

