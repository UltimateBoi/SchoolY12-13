# NamedTuples are a way of defining a record-like approach in python. They are immutable and can be accessed by attribute names. Here's an example:

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])

person2 = Person(name="Alice", age=25)

print(person2.name)  # Output: Alice
print(person2.age)   # Output: 25

# This approach allow you to create structured data types in Python that resemble records, with named fields and the ability to access them using dot notation. 

# Create a named tuple to represent a student record with fields like name, roll number, and marks. Implement functions to initialize the record, display the record, and calculate the grade based on the marks.

StudentRecord = namedtuple('StudentRecord', ['name', 'roll_number', 'marks'])  # Named tuple to represent a student record with fields like name, roll number, and marks

def initialize_student_record(name: str, roll_number: int, marks: int) -> StudentRecord:  # Function to initialize the student record by creating a named tuple with the given values using the StudentRecord class defined above
    return StudentRecord(name, roll_number, marks)

# Create a named tuple to represent a student record with fields like name, roll number, and marks. Implement functions to initialize the record, display the record, and calculate the grade based on the marks.

StudentRecord = namedtuple('StudentRecord', ['name', 'roll_number', 'marks'])  # Named tuple to represent a student record with fields like name, roll number, and marks

def initialize_student_record(name: str, roll_number: int, marks: int) -> StudentRecord:  # Function to initialize the student record by creating a named tuple with the given values using the StudentRecord class defined above
    return StudentRecord(name, roll_number, marks)

# Define a named tuple to represent an employee record with fields like name, employee ID, department, and salary. Implement functions to add new employees, remove employees, update employee details, and display all employees.

EmployeeRecord = namedtuple('EmployeeRecord', ['name', 'employee_id', 'department', 'salary'])  # Named tuple to represent an employee record with fields like name, employee ID, department, and salary

def add_employee(employees: list, employee_record: EmployeeRecord) -> None:  # Function to add a new employee to the list of employees
    employees.append(employee_record)

# Define a named tuple to represent a book record with fields like ISBN, title, author, and genre. Implement functions to add new books, remove books, update book details, and search for books by ISBN or title.

BookRecord = namedtuple('BookRecord', ['isbn', 'title', 'author', 'genre'])  # Named tuple to represent a book record with fields like ISBN, title, author, and genre

def add_book(books: list, book_record: BookRecord) -> None:  # Function to add a new book to the list of books
    books.append(book_record)

# Create a named tuple to represent a product record with fields like product ID, name, category, and price. Implement functions to add new products, remove products, update product details, and search for products by ID or name.

ProductRecord = namedtuple('ProductRecord', ['product_id', 'name', 'category', 'price'])  # Named tuple to represent a product record with fields like product ID, name, category, and price

# Create a named tuple to represent a bank account record with fields like account number, account holder name, balance, and account type. Implement functions to deposit money, withdraw money, check balance, and transfer money between accounts.

BankAccountRecord = namedtuple('BankAccountRecord', ['account_number', 'account_holder_name', 'balance', 'account_type'])  # Named tuple to represent a bank account record with fields like account number, account holder name, balance, and account type
