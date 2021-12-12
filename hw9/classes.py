class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print("Hello my name is ", self.name, self.surname, "and my age is ", self.age)


# task 2

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        rez = self.age * self.age_factor
        return rez


    # task 3


class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current_channel_number = self.channels[0]

    def first_channel(self):
        self.current_channel_number = self.channels[0]
        return self.current_channel_number

    def last_channel(self):
        self.current_channel_number = self.channels[-1]
        return self.current_channel_number

    def turn_channel(self, channel_number):
        self.current_channel_number = channel_number - 1
        rez = self.channels[self.current_channel_number]
        return rez

    def next_channel(self):
        if self.current_channel_number == len(self.channels) - 1:
            self.current_channel_number = 0
            rez = self.channels[self.current_channel_number]
            return rez
        else:
            self.current_channel_number += 1
            rez = self.channels[self.current_channel_number]
            return rez

    def previous_channel(self):
        if self.current_channel_number == 0:
            rez = self.channels[-1]
            return rez
        else:
            self.current_channel_number -= 1
            rez = self.channels[self.current_channel_number]
            return rez

    def current_channel(self):
        rez = self.channels[self.current_channel_number]
        return rez

    def is_exist(self, n):
        for num, name in enumerate(self.channels):
            if n == num or n == name:
                return "Yes"
        return "No"
