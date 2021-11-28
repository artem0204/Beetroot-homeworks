#
# # task 1
# stroka = "x"
# while len(stroka) >= 2:
#     print(stroka[:2], end='')
#     print(stroka[-2:])
#     break
# else:
#     print("empty string")
#
# # task 2
# phoneNum = "095718747щ"
# if len(phoneNum) == 10 and phoneNum.isdigit():
#     print(phoneNum, "ваш номер телефона правильный")
# else:
#     print("не правильный формат телефона ")
#
# # task 3
# name = "artem"
# inputName = str(input("enter your name: "))
# if name == inputName.lower():
#     print("your name is compared")
# else:
#     print("your name is not compared ")

x = 10
if x < 5:
	print(10 + 10)
elif x > 5:
	print(101 - 202)
elif x == 10:
	print(1/0)
else:
	print(1 * 10)