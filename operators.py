          #operators#


#arthimetic operators#

a = 8
b = 4
print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)  
print("Division:", a / b) 
print("Floor Division:", a // b)  
print("Modulus:", a % b) 
print("Exponentiation:", a ** b)


#relational operators#
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


#logical operator#
a = True
b = False
print(a and b)
print(a or b)
print(not a)


#bitwise operators#
a = 10
b = 2

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


#identity operator#
a = 20
b = 3
c = a

print(a is not b)
print(a is c)


#membership operator#
fruits = ['apple', 'banana', 'mango']

print('apple' in fruits)     
print('grape' not in fruits)

#assignment operator#
x = 10
print("x =", x)
x += 5   # x = x + 5
print("After x += 5:", x)
x -= 3   # x = x - 3
print("After x -= 3:", x)
x *= 2   # x = x * 2
print("After x *= 2:", x)
x /= 4   # x = x / 4
print("After x /= 4:", x)
x %= 3   # x = x % 3
print("After x %= 3:", x)
x = 10
x //= 3
print("After x //= 3:", x)
x **= 2
print("After x **= 2:", x)
