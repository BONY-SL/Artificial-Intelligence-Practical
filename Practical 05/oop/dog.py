class Dog:
    def __init__(self, name, breed, age):
        """Constructor to initialize dog's attributes"""
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        """Method for dog barking"""
        print(f"{self.name} says Woof! Woof!")

    def get_info(self):
        """Method to display dog's details"""
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age} years"


# Creating objects of Dog class
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Beagle", 2)

# Accessing methods
dog1.bark()
print(dog1.get_info())

dog2.bark()
print(dog2.get_info())
