# class definition
class Person:

    # constructor
    def __init__(self, name, age):
        # two properties/attributes
        self.name = name
        self.age = age


# main application
if __name__ == "__main__":
    # Create person object/instance
    p1 = Person("Harry", 24)
    p2 = Person("Cristina", 21)
    p3 = Person("Chiara", 18)

    # what is their name?
    print(p1.name)
    print(p2.name, p2.age)
    print(p3.age)
