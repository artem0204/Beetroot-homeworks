#task1
import random

number = random.randint(1, 10)
numberOfAttempts = 0
while numberOfAttempts < 5:
    guess = int(input("guess a number from 1 to 10: "))
    numberOfAttempts += 1
    if guess < number:
        print("This {0} number is more then the one guessed".format(guess))
    if guess > number:
        print("This {0} number is less  then the one guessed".format(guess))
    if guess == number:
        break
if guess == number:
    print(" Yes this {0} number is right because I thought the number {1}".format(guess,number))
else:
    print("you guessed wrong, it was a number {0} ".format(number))

# task 2
name = input('enter your name: ')
age = int(input("enter your age:"))
age += 1
print("Hello {0}, on your next birthday you’ll be {1} years".format(name,age))

# task3
word = input("enter any word:  ")
i = 1
while i <= 5:
    print("".join(random.sample(word,len(word))))
    i += 1

# task 4
counter = 0
score = 0
count = 0
operators = ['+','-','/','*']
name = input("please enter your name.  ")
print("thanks", name, "lets get startes ")
while counter < 5:
    firstNumber = random.randint(0,10)
    secondNumber = random.randint(0,7)
    operator = random.choice(operators)
    question = print(firstNumber, operator, secondNumber, "=")
    userAnswer = input("Answer: ")
    if operator == "+":
        count = firstNumber + secondNumber
        if count == int(userAnswer):
            print("correct !")
            score += 1
        else:
            print("incorrect !")
    elif operator == "-":
        count = firstNumber - secondNumber
        if count == int(userAnswer):
            print("correct !")
            score +=1
        else:
            print("incorrect !")
    elif operator == "/":
        count = firstNumber // secondNumber
        if count == int(userAnswer):
            print("correct !")
            score += 1
        else:
            print("incorrect")
    elif operator == "*":
        count = firstNumber * secondNumber
        if count == int(userAnswer):
            print("correct !")
            score += 1
        else:
            print("incorrect !")
    counter += 1
print("your quiz is over ")




