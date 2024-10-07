class Student:
    def __init__(self, name, student_id, major):
        self.__name = name
        self.__student_id = student_id
        self.__major = major

    def get_major(self):
        return self.__major

    def set_major(self, major):
        self.__major = major

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Student ID: {self.__student_id}")
        print(f"Major: {self.__major}")

# Testing the Student class with example data (data would be better stored in a database)
student1 = Student("Jeff Bezos", "S12345", "Computer Science")
student2 = Student("Bob Smith", "S67890", "Mathematics")

# Display initial information
student1.display_info()
print()
student2.display_info()

# Change major for student2 and display updated information
student2.set_major("Physics")
print("\nAfter changing major:")
student2.display_info()