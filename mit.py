# input = ("type literally anything")

# 5 != 4

#x=1
#print(x)
#x_str = str(x)

#print("my favorite number is "+x_str+"."+" x =",x)

#text = input("type anything: ")
#print(5*text)

#num = int(input("type a number: "))
#print(5+num)

#temp = 120
#if temp > 85:
#   print("Hot")
#elif temp > 100:
#   print("REALLY HOT!")
#elif temp > 60:
#   print("Comfortable")
#else:
#   print("Cold")

#n = 0.0
#while n < 5:
#    print(n)
#    n = n+1.0

#for n in range(1,11):
#    if n % 2 == 0:
#        print(n)
#print('Goodbye!')


#mysum = 0
#for i in range(7, 10):
#    mysum += i
#print(mysum)

#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#print(mysum)

#happy = 0
#for i in range(>2):
#        print('hello world')

#if happy > 2:
#    print('hello world')

#num = 0
#while num <= 5:
#    print(num)
#    num += 1

#print("Outside of loop")
#print(num)

# INFINITE LOOP
#numberOfLoops = 0
#numberOfApples = 2
#while numberOfLoops < 10:
#    numberOfApples *= 2
#    numberOfApples += numberOfLoops
#    numberOfLoops -= 1
#print("Number of apples: " + str(numberOfApples))

#num = 10
#while num > 3:
#    num -= 1
#    print(num)

#num = 10
#while True:
#    if num < 7:
#        print('Breaking out of loop')
#        break
#    print(num)
#    num -= 1
#print('Outside of loop')

# INFINITE LOOP
#num = 100
#while not False:
#    if num < 0:
#        break
#print('num is: ' + str(num))

#n = 2
#while n<=11:
#    print(n)
#    n += 2
#print('Goodbye!')

#print('Hello!')
#n = 10
#while n > 1:
#    print(n)
#    n -= 2

#end = 6
#n = 0
#x = 0
#while n <= end:
#    x += n
#    n += 1
#print(x)

#print('Hello!')
#for n in range(0, 10, 2): #the last number tells FOR what the count is per iteration
#    print(10 - n)

#total = 0
#end = 500
#for next in range(1, end+1):
#    total += next
#print(total)

#x = 3
#ans = 0
#itersLeft = x
#while(itersLeft != 0):
#    ans = ans + x
#    itersLeft = itersLeft - 1
#print(str(x) + '*' + str(x) + ' = ' + str(ans))

#num = 10
#for num in range(5):
#    print(num)
#print(num)

#divisor = 2
#for num in range(0, 10, 2):
#    print(num/divisor)

#for variable in range(20):
#    if variable % 4 ==0:
#            print(variable)
#    if variable % 16 == 0:
#        print('Foo!')

#for letter in 'hola':
#    print(letter)


#count = 0
#for letter in 'Snow!':
#    print('Letter # ' + str(count) + ' is ' + str(letter))
#    count += 1
#    break
#print(count)

#greeting = 'Hello!'
#count = 0

#for letter in greeting:
#    count += 1
#    if count % 2 == 0:
#        print(letter)
#    print(letter)

#print('done')


#school = 'Massachusetts Institute of Technology'
#numVowels = 0
#numCons = 0

#for char in school:
#    if char == 'a' or char == 'e' or char == 'i' \
#       or char == 'o' or char == 'u':
#        numVowels += 1
#    elif char == 'o' or char == 'M':
#        print(char)
#    else:
#        numCons -= 1

#print('numVowels is: ' + str(numVowels))
#print('numCons is: ' + str(numCons))


# MOTHERFUCKINNG INTERATIVE LOOPS

x = int(input('enter an integer '))
ans = 0
while ans**3 < abs(x):
    ans = ans+1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('cube root of ' + str(x) + ' is ' + str(ans))


cube = int(input('enter an integer '))
for guess in range(abs(cube+1)):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, ' is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('cube root of ' +str(cube)+ ' is ' + str(guess))
