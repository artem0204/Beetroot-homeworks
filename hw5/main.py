# task 1

someStr = "Hello my name is Artem"
isDict = dict()
wordsList = someStr.split()
for i in wordsList:
    if i in isDict:
        isDict[i] += 1
    else:
        isDict[i] = 1
print(isDict)

# task 2
stock = {"banana": 6,"aplle": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "aplle": 2, "orange": 1.5, "pear":3}
i = 0
for key in prices:
    i += prices[key] * stock[key]
print(i)



# task 3

a_list = [(x, x**2) for x in range(1,11)]
print(a_list)



