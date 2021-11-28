import random

# task 1
list1 = []
i = 1
while i <= 10:
    num = random.randint(1,10)
    list1.append(num)
    i += 1
print(list1)
print(max(list1))

# task 2
list2 = []
j = 1
while j <= 10:
    num1 = random.randint(1,10)
    list2.append(num1)
    j += 1
print(list2)
list3 = list(set(list1) & set(list2))
print(list3)

# task 3
a = []
b = []
for t in range(1,101):
    a.append(t)
    if t % 7 == 0 and t % 5 != 0:
        b.append(t)
print(a)
print(b)

