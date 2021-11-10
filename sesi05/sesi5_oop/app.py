class Dog:
    # Class attribute
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.breed = breed
    
    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# buddy = Dog("Buddy", 9)
# miles = Dog("Miles", 4)

# print(buddy.name)
# print(buddy.age)
# print(buddy.species)

#-------------------
# miles = Dog("Miles", 4)
# print(miles.description())
# print(miles.speak("Woof Woof"))
# print(miles.speak("Bow Wow"))

#----example
# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")
# print(buddy.speak("Yap"))
# print(jim.speak("Woof"))

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))
print(miles.speak())
print(miles.speak("Grrr"))