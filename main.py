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
dog_name = input("What is your dog's name? ")
dog_colour = input("What is the colour of your dog? ")
doggo = Dog(dog_name, dog_colour)

# Output its name and colour in a single message
doggo.dog_info()

# Make the dog woof 10 times
doggo.woof(10)

# Output the memory location of the Dog object
print(f"The memory location of the Dog object is: {hex(id(doggo))}")