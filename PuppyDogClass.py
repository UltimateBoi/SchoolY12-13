class Dog:
    def __init__(self, name, colour):
        self._name = name
        self._colour = colour

    def bark(self, times):
        for _ in range(times): # Loop for the number of times specified using the underscore as a throwaway variable
            print("Woof!")

    def get_name(self): # Getter for name attribute
        return self._name

    def set_name(self, name): # Setter for name attribute
        self._name = name

    def get_colour(self): # Getter for colour attribute
        return self._colour

    def set_colour(self, colour): # Setter for colour attribute
        self._colour = colour


# The Puppy class is a subclass of Dog. It inherits Dogs attributes and methods
class Puppy(Dog):
    def __init__(self, name, colour): 
        super().__init__(name, colour) # Initialize inherited attributes from Dog
        self._shoesChewed = 0 # New attribute for Puppy

    # Override bark method to implement polymorphism: puppies yap instead of woof
    def bark(self, times): # Overridden method for bark specific to Puppy
        for _ in range(times):
            print("Yap!")  # Print the puppy bark instead from Dogs bark

    def chewShoe(self, count): # New method specific to Puppy
        self._shoesChewed += count

    def get_shoesChewed(self):
        return self._shoesChewed

    def set_shoesChewed(self, count):
        self._shoesChewed = count


if __name__ == "__main__":
    dog = Dog("Fido", "Brown") # Instantiate a Dog and display its details
    print(f"Hello {dog.get_name()}, you are a {dog.get_colour()} colour.")  # Output dogs details

    puppy = Puppy("Buddy", "Golden") # Instantiate a Puppy and display its details
    print(f"Hello {puppy.get_name()}, you are a {puppy.get_colour()} colour.")  # Output puppys details

    print("Dog:")
    dog.bark(3) 

    print("Puppy:")
    puppy.bark(3)
    
    puppy.chewShoe(2)
    print(f"{puppy.get_name()} has chewed {puppy.get_shoesChewed()} shoes.") # Output updated puppy attribute