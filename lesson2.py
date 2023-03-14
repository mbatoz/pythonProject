#compare = 3 == 4
#compare1 = 3 != 4
#print(compare)
#print(compare1)
import sys

#x = 3
#print(x > 3 and x < 8)
#print(x >3 and x > 8)

#print(x > 3 or x < 8)
#print(x > 3 or x > 8)

#print(x > 3 and not x < 8)
#print(x > 3 and not x > 8)

#if x == 5:
#    print('Five')
#else:
#    print('Not five')
#
#if x == 5:
#    print('Five')
#elif x > 5:
#    print('More than five')
#else:
#    print('Less than five')

#age = int(input('Please, enter your age: '))
#if age >= 18:
#    print('Welcome')
#else:
#    print('Go home, baby')

# num1 = 0
# num2 = 0
# try:
#    num1 = int(input('Number 1: '))
#    num2 = int(input('Number 2: '))
# except ValueError:
#    print('Please, insert number')
#    sys.exit()
# operator = input('Operator: ')
# if (num2 == 0 and operator == '/') or num1 > 5:
#    try:
#        result = num1 / num2
#       print(f'Result = {result}')
#    except ZeroDivisionError:
#        print('На ноль делить нельзя')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')
#
# if num1 == 'a':
#     print('Please, insert number')

# num = 0
# while num < 5:
#     print(num)
#     num += 1

# message = "Hello"
# i = 1
# while i < 6:
#     print(i, message)
#     if i == 3:
#         break
#     i += 1

# message1 = "Success"
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message1)

# for i in range(6):
#     print(i)

# for i in range(1, 6, 2):
#     print(i)

# for item in "Hello":
#     print(item)
#
# message = 'Hello'
# print(message[1: 5: 2])

# def num():
#     return 2 * 2
# start = num()
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)

# i = 0
# x = 0
# while i < 4:
#     x += i
#     i += 1
#     print(f"x = {x}, i = {i}")

# message = ''
# if message:
#     print(message)
# else:
#     print('The string is empty')

# num = 4
# if num%2:
#     print('Odd')
# else:
#     print('Even')

def num(num1, num2):
    return num1 - num2

print(num(10, 5))
print(num(9, 7))