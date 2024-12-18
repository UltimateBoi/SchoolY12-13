class Dog:
  def __init__(self, name, colour):
    self._name = name
    self._colour = colour

  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def get_colour(self):
    return self._colour

  def set_colour(self, colour):
    self._colour = colour

  def dog_info(self):
    print(f"Hello {self._name}, you are a {self._colour} colour.")

  def woof(self, times):
    print("Woof! " * times)

# Initialize a new instance of a dog
# dog_name = input("What is your dog's name? ")
# dog_colour = input("What is the colour of your dog? ")
# doggo = Dog(dog_name, dog_colour) # Setting to user input
doggo = Dog("Jeff", "Brown") # Setting by deafult to reduce test times
doggo2 = doggo
doggo3 = Dog("Bill", "White")

print(doggo2.get_name(), end="\n\n")

print(hex(id(doggo)))
print(hex(id(doggo2)), end="\n\n")

print(hex(id(doggo._colour)))
print(hex(id(doggo2._colour)), end="\n\n")

doggo2.set_colour("Black")
doggo2.set_name("Bob")

print(doggo._colour)
print(doggo2._colour, end="\n\n")

print(hex(id(doggo._colour)))
print(hex(id(doggo2._colour)), end="\n\n")

# Output its name and colour in a single message
# doggo.dog_info()

# Make the dog woof 10 times
# doggo.woof(10)

# # Output the memory location of each object within the Dog class
# print(f"The memory location of the Dog object is: {hex(id(doggo))}")
# print(f"The memory location of the Dog get_name object is: {hex(id(doggo.get_name))}")
# print(f"The memory location of the Dog set_name object is: {hex(id(doggo.set_name))}")
# print(f"The memory location of the Dog colour object is: {hex(id(doggo.get_colour))}")
# print(f"The memory location of the Dog set_colour object is: {hex(id(doggo.set_colour))}")
# print(f"The memory location of the Dog info object is: {hex(id(doggo.dog_info))}")
# print(f"The memory location of the Dog woof object is: {hex(id(doggo.woof))}")