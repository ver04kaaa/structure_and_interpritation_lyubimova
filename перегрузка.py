class Person:
    def __init__(self, name=None, age=None):
        if name is None and age is None:
            print("No arguments provided")
        elif name is not None and age is None:
            print("Name is:", name)
        elif name is None and age is not None:
            print("Age is:", age)
        else:
            print("Name is:", name)
            print("Age is:", age)

person1 = Person()
person2 = Person("Alice")
person3 = Person(age=25)
person4 = Person("Bob", 30)