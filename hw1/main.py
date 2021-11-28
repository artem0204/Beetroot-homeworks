# Home Work 1 from LMS
# task2

# sep
task2 = "baj"
print(task2, task2, task2, sep='\n')


# end
task21 = "rih"
print(task21, task21, task21, end='\t')
print(task2)

# task3

num = '#'
print(num*9)
print('#\t\t#\n'*3, end='')
print(num*9)
print()
print('#\t\t#\n'*2, end='')
print(num*9)
print('#\t\t#\n'*2)

# HomeWork 2 from LMS
# task1
import math

name = "Artem"
day = "Monday"
print('Good day '+name+"! " + day+" is a perfect day to learn some python.")

# task2

firstName = 'atrem'
lastName = "podgorniy"
result = firstName+" "+lastName
print(result)

# task3

num1 = -8
num2 = -3

# Addition
print(num1 + num2)

# Subtraction
print(num1 - num2)

# Division
print(num1 / num2)

# Multiplication
print(num1 * num2)

# Exponent (Power)
print(num1 ** num2)

# Modulus
print(abs(num1))
print(abs(num2))

# Floor division
print(num1 // num2)

# HomeWork from Git

# 1

tottal = 44
rez = (tottal * 80)//100
print("Для успешного окончания курса надо сдать {} домашек".format(rez))

# 2
x1 = 2
y1 = 4

x2 = 5
y2 = 3

result = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print(result)

# 3

var1 = 'pyThoN'
print(str.capitalize(var1))

print(var1.lower())
print(var1.upper())

# 4

price = 12
weight = 3.4121
rez = round(price*weight,2)
print(rez)

# 5

number = 12
username = "ираклий"
access_mask = 54
hour_price = 15.321
rez="0000"+str(number)+'\t'+username.capitalize()+'\t'+bin(access_mask)[2:]+'\t'+str(round(hour_price, 2))
print(rez)

# 6

a=10
b=55
a+=45
b-=45
print(a,b)




