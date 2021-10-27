class Dog:
    legs = 4

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def speak(self, sound):
        return f"The {self.color} {self.breed} says: {sound}"


if __name__ == "__main__":
    d1 = Dog("Husky", "White")
    d2 = Dog("Bulldog", "Brown")

    print(d1.speak("Hello woof woof Everyone!"))
    print(d2.speak("Where is my treat?"))
