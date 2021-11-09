# print('file')
# try:
#     #    f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
#     with open("sample.txt", 'r', encoding='utf-8') as f:
#         print("opened!")
#         # write
#         # f.write("my first file\n")
#         # f.write("This file\n\n")
#         # f.write("contains three lines\n")
#         #append
#         # f.write("\nappend new text line\n")
#         #read
#         print(f.read(4)) #first 4 line charac
#         print(f.read(4)) #next 4 line charac
#         print(f.read())     # read in the rest till end of file
#         print(f.read(), "0")  # further reading returns empty string
#         print(f.tell())    # get the current file position
#         print(f.seek(3))   # bring file cursor to initial position
#         print(f.read(5)) #next 4 line charac
#         print(f.seek(0))   # bring file cursor to initial position
#         print(f.readline()) # read until nextline

#     # perform file operations
# finally:
#     f.close()
#     print("closed")


#---------------------------------------------------------------------------------
#exception

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."
# assert ('win32' in sys.platform), "This code runs on Windows only."

#The try and except Block: Handling Exceptions

def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
#     print('The os_interaction() function was not executed')

#------------------
#another example 
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)

#mix
# try:
#     os_interaction()
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     print(error)
#     print('os_interaction() function was not executed')

#else clause -- else will run if no exception whent try
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)


#Cleaning Up After Using finally - finally will always run


try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')