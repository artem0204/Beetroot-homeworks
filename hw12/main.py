if __name__ == '__main__':
    # task1
    def num_loc_var():
        a = 1
        b = 2
        c = 3


    print(num_loc_var.__code__.co_nlocals)


    # task2
    def first_func(func):
        return func


    def test_func():
        print("This is function in another function ")


    first_func(test_func())


    # task 3
    def choose_func(nums, func1, func2):
        for num in nums:
            if num > 0:
                return func1(nums)
            else:
                return func2(nums)


    def square_nums(nums):
        return [num ** 2 for num in nums]


    def remove_negatives(nums):
        return [num for num in nums if num > 0]


    listOfNums = [-3, -2, 4, 5]
    print(choose_func(listOfNums, square_nums, remove_negatives))


