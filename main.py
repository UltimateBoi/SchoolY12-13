def __init__():
    class Dog:
      def __init__(dog, name, colour):
        dog.name = name
        dog.colour = colour
      def dogInfo(x):
        print("Hello", x.name + ", You are a", x.colour, "colour.")

    dogName = input("What is your dogs name? ")
    dogColour = input("What is the colour of your dog? ")
    doggo = Dog(dogName, dogColour)
    doggo.dogInfo()
__init__()