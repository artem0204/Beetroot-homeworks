from classes import Person, Student, Teacher, Mathematician, Product,ProductStore,CustomExeption

if __name__ == '__main__':
    # task 1
    person = Person("Nastya", "Gavrilova", "20")
    person.display_person()
    student = Student("Mark", "Vasilev", "17")
    student.subjects = ["mathematics", "Economics", "Physics"]
    student.grade = ["5", "4", "3"]
    student.display_student()
    teacher = Teacher("Anna", "Kosenko", "46")
    teacher.salary = 16000
    teacher.position = "proffesor"
    teacher.display_Teacher()

    #     task 2
    mathematic = Mathematician()
    listNums = [3, 60, 32]
    print(mathematic.square_nums(listNums))
    listNums1 = [-3, 2, -6, 5, -8]
    print(mathematic.remove_positives(listNums1))
    listLeaps = [1988, 2020, 2025, 2008, 1913]
    print(mathematic.filter_leaps(listLeaps))

#    task 3
    product1 = Product("Sport","football tshirt", 330)
    product2 = Product("Vegatabls","Tomato",12)
    productStore = ProductStore()
    print(productStore.add(product1,3))


# task 4
try:
    msg = input("enter something")
    if msg.isupper():
        raise CustomExeption(msg)
except:
    my_file = open("exceptions.txt", "w+")
    my_file.write(f"error: {CustomExeption(msg)} ")
    my_file.close()
