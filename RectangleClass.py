class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

# Testing the Rectangle class
rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 2)

print(f"Rectangle 1 - Length: 5, Width: 3")
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")

print(f"\nRectangle 2 - Length: 10, Width: 2")
print(f"Area: {rect2.area()}")
print(f"Perimeter: {rect2.perimeter()}")