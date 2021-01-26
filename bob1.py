# Variables

#name = "bob"
#number = "1234"
#print(name , number)

# camelCaseConvention  Common in other languages

# underscore_convention  Most common in python (PEP8)

# Types (ints, floats, doubles, strings)

#str = "Hello World" #This is a string
#print(str)

#int = 123 #This is an integer
#print(int)

#int = -123 #This is also an integer
#print(type(int))

#real_num = 3.14156 #This is a float, as in floating point number
#print(type(real_num))

#a = 3.4
#b = 3.9
#print(a , b) #Floats round DOWN to the next lower integer

#c = -3
#print(float(c)) #This can convert an integer into a float

# Basic Operators for arithmetic




# Loops

# Prime number checker


#for n in range(-10, 100):
    #n = int(input("n= "))
#    if n >= 1:
#        divisors = []
#        for divisor in range(2, n):
#            if n % divisor == 0:
#                divisors.append(divisor)

#        if len(divisors) == 0: # prime
#            print("{:d} is prime.".format(n))
#        else:
#            print("{:d} is not prime because {:} divide {:d}".format(n, str(divisors), n))
#    else:
#        print("{:d} is not prime.".format(n))


# Loops with conditionals

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#total = 0
#for n in numbers:
#    if n % 2 == 0: # check is n is a multiple of 0, or % attempts to divide by 2 until 0 is reached
#        total = total + n #same as total += n
#        total += n
#print(total)

#alpha = 'abcdefghijklmnopqrstuvwxyzABCEDEFGHIJKLMNOPQRSTUVWXYZ'
#vowels = 'aeiouAEIOU'
#my_string = "I like perky tits."

#char = []
#for ch in my_string:
#    if ch not in vowels and ch in alpha:
#        char.append(ch)
#const = ''.join(char)
#print(const)


# Iterables

#my_list = [1,2,3,4,5]
#my_tuple = (2,7,8,9,10)
#my_string = "Nice tits"

#print('__iter__' in dir(my_list))
#print('__iter__' in dir(my_tuple))
#print('__iter__' in dir(my_string))

#list_iterator = iter(my_list)
#while True:
#    try:
#        next_elem = next(list_iterator)
#        print(next_elem)
#    except StopIteration:
#        break

# While
#index = 0
#names = ["Josh", "Bob", "Larry", "Hooker"]


#print("Input two numbers which add up to 20 fucko")
#while True:
#    a, b = int(input("a: ")), int(input("b: "))
#    if a + b ==20:
#        print("Good job, moron")
#        break
#    else:
#        print("That doesn't equal 20, retard.")

#while index < len(names):
#    name = names[index]
#    print(name)
#    index = index + 1

# 1 - 10
#total = 0
#v = 1
#while v <= 10:
#    total = total + v
#    v = v + 1
#print(total)


# Example of using "in" to check T/F
#s= "hello fucker"
#a = [4,6,9]

#print(5 in a)
#print(4 in a)
#print("fuck" in s)

#for even_number in [2,4,6,8,10]:
#    print(even_number)

#odds = [3,1,5,7,9,11]
#for odd_number in odds:
#    print(odd_number)

#print(range(len(odds)))
#for index in range(len(odds)):
#    print("Index: {:d}, odd number: {:d}".format(index, odds[index]))




# Conditionals

# Examples of conditionals

# 5*7, -3-9, 4+2, 6/5, 6*6, 3/0, 5(2
#import sys #sys.exit quits program

#line = input()
#split = line.split()

#if len(split) != 3:
#    print("Wrong format.")
#    sys.exit()

#left = int(split[0])
#op = split[1]
#right = int(split[2])

#val = 0

#if op == '+':
#    val = left + right
#elif op == '-':
#    val = left - right
#elif op == '*':
#    val = left * right
#elif op == '/':
#    if right == 0:
#        print("Division by zero will break the universe.")
#        sys.exit()
#    val = left / right
#else:
#    print("Unknown operator: {operator}".format(operator=op))
#    sys.exit()

#print("{line_expr} = {value:.2f}".format(line_expr=line, value=val))


#a, b = int(input("a = ")), int(input("b = "))
#if a % b == 0 or b % a ==0:
#    print("divisible")

#a, b = int(input("a = ")), int(input("b = "))
#if b != 0: print(a/b)
#if b is not 0: print(a/b)
#if not(b ==0): print(a/b)

#name1 = input("name1: ")
#name2 = input("name2: ")
#name3 = input("name3: ")

#if name1.lower() == name2.lower() == name3.lower():
#    print("equal")
#else:
#    print("not equal")

# AND, OR, and NOT

#T = True
#F = False

#statement1 = 3 > 4 # False
#statement2 = 10 % 5 == 0 # True
#statement3 = "A".lower() == "a" # True
#print(statement1, statement2, statement3)

# or
#if F or F: print("F or F")
#if F or T: print("F or T")
#if T or F: print("T or F")
#if T or T: print("T or T")
#print("")

# and
#if F and F: print("F and F")
#if F and T: print("F and T")
#if T and F: print("T and F")
#if T and T: print("T and T")

# not
#if not F: print("not F")
#if not T: print("not T")

#print(not(3==6))
#print(not(3!=6))

#print("Input and integer:  ")
#n = int(input())
#if n < 20:
#    print("n < 20")
#elif n < 40:
#    print("n < 40")
#elif n < 60:
#    print("n < 60")
#else:
#    print("n >= 60")



#name = "Sarah"
#if name == "John":
#    print("John")
#else:
#    print("name is not John")
#if name == "Emily":
#    print("Emily")
#elif name == "Mike":
#    print("Mike")
#elif name == "Bob":
#    print("Bob")
#else:
#    print("You are not Emily, Mike, or Bob.")

#tmp = """
#(-∞ , -30] REALLY COLD!
#(-30, 0)   cold
#0          zero
#(0, 20)    perfect
#[20, 40)   hot
#[40, ∞)    REALLY HOT"""
#print(tmp)

#print("What is the current temperature?")
#t = int(input())

#if (t <= -30):
#    print("REALLY COLD!")
#if (t < 0):
#    if (t > -30):
#        print("cold")
#if (t == 0):
#    print("zero")
#if (t > 0):
#    if (t < 20):
#        print("perfect")
#if (t >= 20):
#    if (t < 40):
#        print("hot")
#if (t >= 40):
#    print("REALLY HOT!")


#print("What is your age?")
#age = int(input())	#This has to have int() around input because the console takes in numbers as strings.
#if age >= 30:
#    print("Age is too old.")

#else:
#    print("That'll do donkey.")

#name = "Slut"
#if name == "Slut":
#    print("Yes, I'm a slut.")
#    if age >= 30:
#         print("I'm a worn out slut.")


# List slicing: used to query only a part of any array.

#a = list(range(0, 10))
#print(a)

# print(a[2:len(a)]) == print(a[2:]) Booth print starting at the 2nd index position and through the ende of the list.

#print(a[::2]) # prints every other entry.

#print (a[0:6:2]) # prints every other entry, but stops at 6th one.

#print(a[-1]) # counts backwards from the end.

#print(a[2:-2]) # prints all between 2 and the send to last (8)

#print(a[::-1]) # prints array in reverse order



# 2D arrays

#from pprint import pprint as pretty_print

#from copy import copy, deepcopy

# This is an array of arrays (designated by the brackets)

#nums_2d = [
#	[1,2,3,4,5,6,7],
#	[8,9,10,11,12,13,14,15],
#	[16,17,18,19,20,21,22]
#]

#print(nums_2d[1][3])
#print(nums_2d)
#pretty_print(nums_2d)

#nums_2d[2][1] = -5
#pretty_print(nums_2d)

#letters = ['a','b','c','d','e']
#letters_2d = [copy(letters), copy(letters), copy(letters)]

#pretty_print(letters_2d)
#letters_2d[0][0] = 'f'
#pretty_print(letters_2d)


# Lists and manipulation thereof.

# min, max, sum, len

#numbers = [3.14, -5, 10, 10**4, 17 ]
#hello_world = "HelloWorld"

#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))
#print(len(numbers))

#print(max(hello_world))
#print(min(hello_world))
##print(sum(hello_world))  Can't sum a string.
#print(len(hello_world))



# sorting lists and strings
#alpha1 = ['a', 'f', 'b', 'e', 'd']
#alpha2 = ['g', 'i', 'h']
#alpha3 = 'jklmnopqrstuvwxyz'

#alpha1.sort()
#alpha2.sort()
#alpha3.sort()
#print(alpha1)
#print(alpha2)
#alpha1.insert(2, 'c')
#print(alpha1 + alpha2)

#alpha1 =''.join(alpha1)
#alpha2 =''.join(alpha2)
#print(alpha1 + alpha2)

#alphabet = alpha1 + alpha2 + alpha3
#print(alphabet)


#alpha =["a", "b", "c", "d"]
#alpha.append("e")
#alpha=alpha + ["f"]
#print(alpha)
#d_index=alpha.index("d")
#print("d_index " + str(d_index))
#del alpha[3] # [] can be specified by either the d_index, or the index number
#print(alpha)
#alpha.remove("c")
#print(alpha)

#numbers = [5, -6, 2, 4, -5, 1]
#names = ["Heather", "Lauren", "Sara", "Tatiana"]

#print(names)
#del names[1]
#print(names)

#mystr = "Hey sweet tits"
#print(mystr[0])
#print(mystr[10])

# firstname, M., lastname

#first_name = str(input("Please enter your first name: "))
#middle_name = str(input("Please enter your middle name: "))
#last_name = str(input("Please enter your lastst name: "))

#first_name = first_name.capitalize()
#middle_name = middle_name.capitalize()
#last_name = last_name.capitalize()

#name_format = "{first} {middle:.1s} {last}"
#print(name_format.format(first=first_name, middle=middle_name, last=last_name))



#n = 11
#f = 1.205050505
#s = "computer"

#print(f)
#print("my number is {:f}".format(f))
#print("my number is {:.3f}".format(f))
#print("my number is {:.4f}".format(f))
#print("{0} {1} {2}".format(n,f,s))
#print("{name} own(s) {amount} of {object}".format(name = "Bob",amount = n, object = "whores"))


# output types for .format
# e = exponents
# b = binary (base 2), will not accept a float
# o = octal, base 8
# d = decimal, base 10
# x = hexidecimal, base 16
# f = floats, a number other than a whole number
# s= strings, default if no option is specified in .format()


#home/cole/anaconda3/bin/python3.6

#bob1.py

#science = "SCIENCE"
#apple = "apple"


#print(science.lower())
#print(science.title())

#apple = "        apple		"
#apple = apple.strip().upper()
#print(apple)

#prefix = "python is an "
#suffix = "awesome language"

#astr = prefix + suffix
#print(astr)

#astr = astr.replace("language", "snake")
#astr = astr * 2
#astr = astr.replace("snake", "language", 1)
#print(astr)
#print(astr.count("an"))
