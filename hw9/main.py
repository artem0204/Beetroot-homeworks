from classes import Person, Dog,TVController

if __name__ == '__main__':
    # task1
    person1 = Person("Vasyl", "Gavrilov", "23")
    person1.talk()

    # Task 2

    dog1 = Dog(3)
    print(dog1.human_age())

    # task 3

    CHANNELS = ["BBC", "Discovery", "TV1000"]
    tvController1 = TVController(CHANNELS)
    print(tvController1.first_channel())
    print(tvController1.last_channel())
    print(tvController1.turn_channel(2))
    print(tvController1.next_channel())
    print(tvController1.previous_channel())
    print(tvController1.current_channel())
    print(tvController1.is_exist("Discovery"))

