
# Modules in python

# Testing modules



#def first_half(s):
#    return s[:len(s)//2]
#def last_half(s):
#    return s[len(s)//2:]

#if __name__ == '__main__': #This line says we are currently running this script.
#    print("Testing string functions")
#    assert first_half("abcd") == "ab", "First half is failing"
#    assert last_half("abcd") == "cd", "last half is failing"

#print(__name__)


# Creating Modules

#import volumes

#print(dir(volumes))

#from volumes import cube_vol  #or from volumes import * (to import all modules in a given file)

#from volumes import cone_vol

#from volumes import sphere_vol

#print(cube_vol(2,3,4))

#print(sphere_vol(4))

#print(cone_vol(3,4))


#import http.server
#import socketserver

#PORT = 8000

#Handler = http.server.SimpleHTTPRequestHandler

#with socketserver.TCPServer(("", PORT), Handler) as httpd:
#    print("serving at port", PORT)
#    httpd.serve_forever()


# import usage: a function which is stored in a separate file and able to be easily located by the interpreter.

#from math import factorial as f # now "f" is shorthand for factorial

#print(f(4))

#import math
#from math import pi # Imports only the pi function
#from math import *  # Imports all functions in math. Why is this different from "import math"?

#print(math.pi)
#print(math.cos(math.pi))
#print(pi)
#print(sin(pi))


# Functions

# Recursion examples

# Counting the vowels in a string

#def count_vowels(s, i = 0):
#    if (i == len(s)): return 0
#    c = s[i]
#    if c in 'aeiou':
#        return count_vowels(s, i + 1) + 1
#    return count_vowels(s, i + 1) + 0
#print(count_vowels('sup fucker'))
#print(count_vowels('bag of dicks'))

# summing digits in a number

#def digit_sum(n):
#    if n == 0: return 0
#    return digit_sum(n//10) + n % 10

#print(digit_sum(345))

# Print nest fibonnachi
#def fib(n):
#    if n == 0 or n ==1:
#        return 1
#    return fib(n-2) + fib(n-1)

#for i in range(1000):
#    print(fib(i))



# Function recursion, when a function calls itself.

# Recursion call stack

#def double(n):
#    if n == 0:
#        return 0
#    return double(n - 1) + 2

#double(5)



# Shift cipher using functions

#alpha = 'abcdefghijklmnopqrstuvwxyz'

#def encrypt(s, shift = 3):
#    encrypted_str = ""
#    for c in s:
#        index = alpha.index(c)
#        shifted_index = (index + shift) % len(alpha)
#        encrypted_str += alpha[shifted_index]
#    return encrypted_str

#def decrypt(e, shift = 3):
#    decrypt_str = ""
#    for c in e:
#        index = alpha.index(c)
#        shifted_index = (index - shift) % len(alpha)
#        decrypt_str += alpha[shifted_index]
#    return decrypt_str

#print(encrypt("nicetits"))
#print(decrypt("qlfhwlwv"))
#print(decrypt(encrypt("fuck")))


# Return and void functions

# If a function returns a value then you can assign a variable to the value.

#def is_even(number):       #This is a return function which checks whether or not a number is even and returns the result.
#    if number % 2 == 0:
#        return True
#    return False

# Return function

#def reverse(s):
#    new_str = ""
#    for i in range(len(s)):
#        new_str += s[len(s) - i -1]
#    return new_str

#print(reverse("123456789"))
#print(reverse("abcdefghij"))
#print(reverse("987654321"))

#def is_palindrome(p):
#    for i in range(len(p)//2):
#        if p[i] != p[len(p) - i - 1]:
#            print("Not a palindrome")
#            return # used to exit function
#    print("Yes, is palindrome")

#is_palindrome("aghhga")
#is_palindrome("123456654321")
#is_palindrome("1")
#is_palindrome("your're a cunt")




#print("This shit recieved no input, I'm just spitting it out")     #This is a void function, it simply does a thing regardless of any input to a variable.





# Arguments and parameters

#import datetime as dt

#def record_time( message, time = dt.datetime.now() ):
#    print("{:}, time: {:}".format(message, time))

#record_time("It is the morning")
#record_time("It is the morning", "February 22nd, 1998")


#def add(a, b, c):
#    return a+b+c

#print(add(1,2,3))

# Variadict functions

#def add(*numbers):
#    total = 0
#    for n in numbers:
#        total += n
#    return total

#print(add(1,2,3,4,5,6))

#PI = 3.141592

#print(5*5*PI) # Hard way, numbers have to be changed every time

#def circle_area(r):
#    return PI*r*r

#print(circle_area(5))
#print(circle_area(10))